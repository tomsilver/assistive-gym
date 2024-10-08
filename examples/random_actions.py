import gym, assistive_gym

env = gym.make('DrinkingJaco-v1', render=True)
observation = env.reset()

while True:
    action = env.action_space.sample() # Get a random action
    print(action)
    observation, reward, terminated, truncated, info = env.step(action)
