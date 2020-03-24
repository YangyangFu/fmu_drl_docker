# set visualise=True requires the docker to render on X11 server.
def test_gym(visualize=True):
    import gym
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(1000):
        if visualize:
            #env.render(mode='rgb_array')
            env.render()
        env.step(env.action_space.sample())
    env.close()
    print("OpenAI Gym is available and successfully working.")


if __name__ == '__main__':
    test_gym()
