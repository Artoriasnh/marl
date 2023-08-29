import numpy as np
from ppo_torch import Agent
from Peartree_env_v15 import PeartreeEnv
from Plot_data_Peartree import *
from save_result_as_csv import *
import pickle

if __name__ == '__main__':
    env = PeartreeEnv()
    N = 1500
    # agent = Agent(n_actions=13, batch_size=10,
    #               alpha=0.01, n_epochs=20,
    #               input_dims=[len(env.low)])


    best_score = env.reward_range[0]
    score_history = []
    avg_score_ = []
    actions = []
    steps = []
    x_ = []

    learn_iters = 0
    avg_score = 0
    n_steps = 0

    # 保存代理模型
    filename = "agent/agentppo.pkl"
    with open(filename, "rb") as f:
        agent = pickle.load(f)

    observation = env.reset()
    done = False
    total_reward = 0

    rewards = []  # 存储每个回合的奖励值
    threshold = 0.1  # 收敛的阈值
    window_size = 10  # 平均奖励计算的窗口大小
    convergence_episode = 0  # 收敛所需的回合数
    episode = 0
    figure_file = 'plots/testppo.png'

    while not done:
        action = agent.choose_action(observation)
        observation_, reward, done, info = env.step(action)
        total_reward += reward
        episode += 1
        rewards.append(reward)

        # 计算平均奖励
        if len(rewards) >= window_size:
            avg_reward = sum(rewards[-window_size:]) / window_size

            # 检查是否达到收敛条件
            if abs(avg_reward - rewards[-1]) < threshold:
                convergence_episode = episode - window_size + 1
                print(avg_reward)
                break

        score_history.append(reward)
        avg_score = np.mean(score_history[-100:])
        avg_score_.append(avg_score)
        x_.append(episode)

        # if avg_score > best_score:
        #     best_score = avg_score
        #     agent.save_models()

    x = [i + 1 for i in range(len(score_history))]

    plot_learning_curve(x, score_history, figure_file)
    build_reward_episode(x_, score_history)
    print(convergence_episode)



