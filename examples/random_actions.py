import gym, assistive_gym
import numpy as np
import pybullet as p

env = gym.make('HumanTesting-v1', render=True)
observation = env.reset()

while True:
    p.stepSimulation(physicsClientId=env.id)

while True:
    action = env.action_space.sample() # Get a random action
    observation, reward, terminated, truncated, info = env.step(action)
