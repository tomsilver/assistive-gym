import gym, assistive_gym

env = gym.make('DrinkingJaco-v1')
observation = env.reset()
# env.render()

while True:
    # env.render()
    action = env.action_space.sample() # Get a random action
    observation, reward, terminated, truncated, info = env.step(action)
