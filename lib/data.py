from env import FourRoom
from agent import QLearning
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import argparse
import random
import itertools

def evaluate_policy(goal, n_episodes=1000, max_length=1000):
    env = FourRoom(p_failure=0.1, reward=goal)
    V = np.zeros(env.state_space)
    for i_episode in range(n_episodes):
            observation = env.reset()
            for t in range(max_length):
                action = np.random.choice(env.action_space)
                new_observation, reward, done, info = env.step(action)
                x, y = observation
                new_x, new_y = new_observation
                V[x,y] += 0.05*(reward + 1.*V[new_x, new_y] - V[x,y])
                observation = new_observation
                if done:
                    #print("Episode finished after {} timesteps".format(t+1))
                    break
    V[goal] = 1
    return V

def create_dataset(output):
    env = FourRoom(p_failure=0.1)
    goals = list(itertools.product([1,2,3,4,5,7,8,9,10,11], [1,2,3,4,5,7,8,9,10,11])) + [(3,3), (6,3), (3,6), (6,6)]
    data = np.zeros((len(goals), len(goals)))

    for i, g in tqdm(enumerate(goals), total=len(goals)):
        data[:,i] = evaluate_policy(g)[env.border==0]

    np.save(output,data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output', help='The path where to save dataset.')
    args = parser.parse_args()
    create_dataset(args.output)
