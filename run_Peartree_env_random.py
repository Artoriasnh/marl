import numpy as np
from ppo_torch import Agent
from Peartree_env_v16 import PeartreeEnv
from Plot_data_Peartree import *
from save_result_as_csv import *

if __name__ == '__main__':
    env = PeartreeEnv()
    N = 1500
    agent = Agent(n_actions=13, batch_size=10,
                  alpha=0.01, n_epochs=20,
                  input_dims=[len(env.low)])

    Episodes = 600

    figure_file = 'plots/new_628v15_rewardrandom-600.png'

    best_score = env.reward_range[0]
    score_history = []
    avg_score_ = []
    actions = []
    steps = []
    x_ = []

    learn_iters = 0
    avg_score = 0
    n_steps = 0

    # agent.load_models()
    for i in range(Episodes):
        observation = env.reset()
        done = False
        score = 0
        scorelist = []
        action = env.action_space.sample()
        while not done:
            env.update_time()
            # print("step:", sp)
            print("episode:", i)
            print("action:", action)
            print("time:", env.state_t)
            observation_, reward, done, info = env.step(action)

            print("reward:", reward)
            n_steps += 1
            score = reward
            # print("steps:", n_steps)
        score_history.append(score)
        avg_score = np.mean(score_history[-100:])
        avg_score_.append(avg_score)
        x_.append(i)

        # if avg_score > best_score:
        #     best_score = avg_score
        #     agent.save_models()

    x = [i + 1 for i in range(len(score_history))]

    plot_learning_curve(x, score_history, figure_file)
    build_reward_episode(x_, score_history)
    # time_in_env(env)
