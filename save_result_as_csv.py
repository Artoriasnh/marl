import csv
import numpy as np


def build_reward_episode(episode, reward):
    data1 = episode
    data2 = reward

    with open('result_csv/railway_rl_reward75ppo120.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(header)

        for w in range(len(data1)):
            # print(w)
            writer.writerow([data1[w], data2[w]])


def build_action_step(step, action):
    data1 = step
    data2 = action

    with open('result_csv/railway_rl_action75ppo120.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(header)

        for w in range(len(data1)):
            # print(w)
            writer.writerow([data1[w], data2[w]])
