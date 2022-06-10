import os
import torch
import pprint
import argparse
import numpy as np
from torch.utils.tensorboard import SummaryWriter

from tianshou.policy import DQNPolicy
from tianshou.utils import TensorboardLogger
from tianshou.env import SubprocVectorEnv
from tianshou.trainer import offpolicy_trainer
from tianshou.data import Collector, VectorReplayBuffer
import torch.nn as nn
import gym
import math

def make_building_env(args):
    import gym_cart_jmodelica

    # make environment and customize some parameters
    env = gym.make(args.task,
                     positive_reward = 2,
                     negative_reward = -100,
                     fmu_result_handling='memory',
                     fmu_result_ncp=10.,
                     filter_flag=False)

    return env

class Net(nn.Module):
    def __init__(self, state_shape, action_shape, nlayers,device):
        super().__init__()
        # define ann
        sequences = [nn.Linear(np.prod(state_shape), 256), nn.ReLU(inplace=True)]
        for i in range(nlayers):
            sequences.append(nn.Linear(256, 256))
            sequences.append(nn.ReLU(inplace=True))
        sequences.append(nn.Linear(256, np.prod(action_shape)))
        self.model = nn.Sequential(*sequences)
        # device
        self.device = device

    def forward(self, obs, state=None, info={}):
        if not isinstance(obs, torch.Tensor):
            obs = torch.tensor(obs, dtype=torch.float).to(self.device)
        batch = obs.shape[0]
        
        logits = self.model(obs.view(batch, -1))
        return logits, state

def test_dqn(args):
    
    env = make_building_env(args)

    args.state_shape = env.observation_space.shape or env.observation_space.n
    args.action_shape = env.action_space.shape or env.action_space.n
    
    print("Observations shape:", args.state_shape)
    print("Actions shape:", args.action_shape)


    # make environments
    train_envs = SubprocVectorEnv(
            [lambda: make_building_env(args) for _ in range(args.training_num)], 
            norm_obs=True)
    test_envs = SubprocVectorEnv(
            [lambda: make_building_env(args) for _ in range(args.test_num)], 
            norm_obs=True, 
            obs_rms=train_envs.obs_rms, 
            update_obs_rms=False)

    # seed
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    train_envs.seed(args.seed)
    test_envs.seed(args.seed)


    # define model
    print(args.state_shape)
    net = Net(args.state_shape, args.action_shape, args.n_hidden_layers, args.device).to(args.device)
    optim = torch.optim.Adam(net.parameters(), lr=args.lr)
    
    # define policy
    policy = DQNPolicy(net, 
                    optim, 
                    args.gamma, 
                    args.n_step,
                    target_update_freq=args.target_update_freq, 
                    reward_normalization = False, 
                    is_double=True)
    
    # load a previous policy
    if args.resume_path:
        policy.load_state_dict(torch.load(args.resume_path, map_location=args.device))
        print("Loaded agent from: ", os.path.join(log_path, 'policy.pth'))

    # collector
    buffer = VectorReplayBuffer(
            args.buffer_size, 
            buffer_num=len(train_envs), 
            ignore_obs_next=True)
    train_collector = Collector(policy, train_envs, buffer, exploration_noise=True)
    test_collector = Collector(policy, test_envs)

    # log
    log_path = os.path.join(args.logdir, args.task)
    writer = SummaryWriter(log_path)
    writer.add_text("args", str(args))
    logger = TensorboardLogger(writer)

    def save_fn(policy):
        torch.save(policy.state_dict(), os.path.join(log_path, 'policy.pth'))

    def train_fn(epoch, env_step):
        # nature DQN setting, linear decay in the first 1M steps
        max_eps_steps = int(args.epoch * args.step_per_epoch * 0.9)

        #print("observe eps:  max_eps_steps, total_epoch_pass ", max_eps_steps, total_epoch_pass)
        if env_step <= max_eps_steps:
            eps = args.eps_train - env_step * (args.eps_train - args.eps_train_final) / max_eps_steps
        else:
            eps = args.eps_train_final
        policy.set_eps(eps)
        print('train/eps', env_step, eps)
        print("=========================")
        #logger.write('train/eps', env_step, eps)

    def test_fn(epoch, env_step):
        policy.set_eps(args.eps_test)

    if not args.test_only:
        # test train_collector and start filling replay buffer
        train_collector.collect(
            n_step=args.batch_size * args.training_num, random=False)
        # trainer
        
        result = offpolicy_trainer(
            policy = policy, 
            train_collector = train_collector, 
            test_collector = test_collector, 
            max_epoch = args.epoch,
            step_per_epoch = args.step_per_epoch, 
            step_per_collect = args.step_per_collect, 
            episode_per_test = args.test_num,
            batch_size = args.batch_size, 
            train_fn=train_fn, 
            test_fn=test_fn,
            #stop_fn=stop_fn, 
            save_fn=save_fn, 
            logger=logger,
            update_per_step=args.update_per_step, 
            test_in_train=False)
        pprint.pprint(result)

    # Lets watch its performance for the final run
    def watch():
        print("Setup test envs ...")
        policy.eval()
        policy.set_eps(args.eps_test)

        buffer = VectorReplayBuffer(
            args.step_per_epoch,
            buffer_num=len(test_envs),
            ignore_obs_next=True,
            save_only_last_obs=False,
            stack_num=args.frames_stack)
        collector = Collector(policy, test_envs, buffer)
        result = collector.collect(n_step=args.step_per_epoch)

        # get obs mean and var
        obs_mean = test_envs.obs_rms.mean
        obs_var = test_envs.obs_rms.var
        print(obs_mean)
        print(obs_var)
        # the observations and action may be normalized depending on training setting
        np.save(os.path.join(args.logdir, args.task, 'his_act.npy'),buffer._meta.__dict__['act'])
        np.save(os.path.join(args.logdir, args.task, 'his_obs.npy'),buffer._meta.__dict__['obs'])
        np.save(os.path.join(args.logdir, args.task, 'his_rew.npy'),buffer._meta.__dict__['rew'])
        np.save(os.path.join(args.logdir, args.task, 'obs_mean.npy'),obs_mean)
        np.save(os.path.join(args.logdir, args.task, 'obs_var.npy'),obs_var)
        rew = result["rews"].mean()
        print(f'Mean reward (over {result["n/ep"]} episodes): {rew}')

    watch()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, default="JModelicaCSCartPoleEnv-v0")
    parser.add_argument('--time-step', type=float, default=0.05)
    parser.add_argument('--seed', type=int, default=0)

    parser.add_argument('--eps-test', type=float, default=0.005)
    parser.add_argument('--eps-train', type=float, default=1.)
    parser.add_argument('--eps-train-final', type=float, default=0.05)

    parser.add_argument('--gamma', type=float, default=0.99)

    parser.add_argument('--n-step', type=int, default=1)
    parser.add_argument('--target-update-freq', type=int, default=100)

    parser.add_argument('--step-per-epoch', type=int, default=1000)
    parser.add_argument('--step-per-collect', type=int, default=1)
    parser.add_argument('--update-per-step', type=float, default=1)

    parser.add_argument('--training-num', type=int, default=1)
    parser.add_argument('--test-num', type=int, default=1)
    parser.add_argument('--logdir', type=str, default='log_ddqn')
    
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--frames-stack', type=int, default=1)
    parser.add_argument('--resume-path', type=str, default=None)
    parser.add_argument('--test-only', type=bool, default=False)

    # tunable parameters  
    parser.add_argument('--lr', type=float, default=0.0003) #0.0003!!!!!!!!!!!!!!!!!!!!!
    parser.add_argument('--epoch', type=int, default=2)
    parser.add_argument('--batch-size', type=int, default=128)
    parser.add_argument('--n-hidden-layers', type=int, default=3)
    parser.add_argument('--buffer-size', type=int, default=50000)

    args = parser.parse_args()

    test_dqn(args)