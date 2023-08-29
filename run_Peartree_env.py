from dqn_pytorch import Agent
from Peartree_env_v15 import PeartreeEnv
from Plot_data_Peartree import *
from save_result_as_csv import *

if __name__ == '__main__':
    env = PeartreeEnv()
    N = 1500
    # agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=env.action_space.n, eps_end=0.01,
    #               input_dims=env.observation_space.shape, lr=0.01)
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=12, eps_end=0.01,
                  input_dims=env.observation_space.shape, lr=0.01)
    Episodes = 600

    figure_file = 'plots/628v15rewarddqn600.png'

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
        done = False
        score = 0
        observation = env.reset()
        action = agent.choose_action(observation)
        while not done:
            env.update_time()
            # action = agent.choose_action(observation)
            # print("step:", sp)
            print("episode:", i)
            print("action:", action)
            print("time:", env.state_t)

            observation_, reward, done, info = env.step(action)
            if done:
                print("done!!!!!!!!!!!")
                break
            else:
                print("reward:", reward)
                n_steps += 1
                score = reward
                agent.store_transition(observation, action, reward, observation_, done)
                # print("steps:", n_steps)
                agent.learn()
                observation = observation_
                actions.append(action)
                steps.append(n_steps)
                build_action_step(steps, actions)
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


    # env.reset()
    # for step in range(steps):
    #     sp = step
    #     x.append(sp)
    #     action = env.action_space.sample()
    #     # print(action)
    #     obs, reward, info, done = env.step(action)
    #     print(reward)
    #     score = reward
    #     score_.append(score)
    #     score_episode_mean = np.mean(score_[-50:])
    #     score_history.append(score_episode_mean)
    #     asc = np.mean(score_history[-50:])
    #     avg_score.append(asc)
    #     # env.render()
    #     if done is True:
    #         env.reset()
