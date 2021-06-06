import gym
import gym_cart_jmodelica

env = gym.make("JModelicaCSCartPoleEnv-v0",
                       m_cart=10,
                       m_pole=1,
                       theta_0=85/180*3.14,
                       theta_dot_0=0,
                       time_step=0.05,
                       positive_reward=1,
                       negative_reward=-100,
                       force=12,
                       log_level=7,
                       fmu_result_handling='file',
                       fmu_result_ncp=100.,
                       filter_flag=False)
states = env.reset()
n_outputs = env.observation_space.shape[0]
print(states)
print(env.tau, env.simulation_start_time)
print(n_outputs)
