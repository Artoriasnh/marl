import os
import math
import numpy as np
import pandas as pd
import random
import gym
import time
from threading import Timer
from gym import error, spaces, utils
from gym.utils import seeding
from constants import *


class PeartreeEnv(gym.Env):
    # metadata = {'render.modes': ['human']}
    def __init__(self):
        self.low = np.array(Low_).astype(np.float32)
        self.high = np.array(High_).astype(np.float32)
        self.action_space = spaces.Discrete(13)
        self.observation_space = spaces.Box(self.low, self.high)
        # self.trainlist = trainlist
        self.state_t = 0
        self.timeStep = 1
        self.episode = 0
        self.state_durations = [25, 95, 455, 755, 1340, 1500]
        self.Peartree_env = np.zeros((18, 18), dtype=np.int64)
        self.pt_env = pd.DataFrame(self.Peartree_env, index=Signal, columns=Signal)


        for i in range(18):
            for j in range(18):
                self.pt_env.loc[Signal[i], Signal[j]] = None
        for i in list(All_routes.keys()):
            self.pt_env[int(All_routes[i][0])][int(All_routes[i][1])] = 0

        self.R11_condition = self.pt_env[Left_signal[7]][Left_signal[4]]
        self.R12_condition = self.pt_env[Left_signal[7]][Left_signal[3]]
        self.R13_condition = self.pt_env[Left_signal[6]][Left_signal[4]]
        self.R14_condition = self.pt_env[Left_signal[6]][Left_signal[3]]
        self.R15_condition = self.pt_env[Left_signal[5]][Left_signal[4]]
        self.R16_condition = self.pt_env[Left_signal[5]][Left_signal[3]]
        self.R17_condition = self.pt_env[Right_signal[5]][Right_signal[6]]
        self.R18_condition = self.pt_env[Right_signal[5]][Right_signal[7]]
        self.R19_condition = self.pt_env[Right_signal[5]][Right_signal[8]]
        self.R20_condition = self.pt_env[Right_signal[5]][Right_signal[9]]
        # R21，R22不存在
        self.R23_condition = self.pt_env[Left_signal[4]][Left_signal[2]]
        self.R24_condition = self.pt_env[Left_signal[4]][Left_signal[1]]
        # R25/26 上面不存在
        self.R27_condition = self.pt_env[Left_signal[3]][Left_signal[2]]
        self.R28_condition = self.pt_env[Left_signal[3]][Left_signal[1]]
        self.R29_condition = self.pt_env[Right_signal[4]][Right_signal[5]]
        self.R30_condition = self.pt_env[Right_signal[3]][Right_signal[5]]
        self.R31_condition = self.pt_env[Right_signal[2]][Right_signal[4]]
        self.R32_condition = self.pt_env[Right_signal[2]][Right_signal[3]]
        self.R33_condition = self.pt_env[Left_signal[2]][Left_signal[0]]
        self.R34_condition = self.pt_env[Left_signal[2]][Left_signal[0]]
        self.R35_condition = self.pt_env[Right_signal[1]][Right_signal[2]]
        self.R36_condition = self.pt_env[Right_signal[0]][Right_signal[1]]

    def update_time(self):
        # if self.episode < self.state_durations[self.episode]:
        if self.state_t < 1500:
            self.state_t += self.timeStep
            # print("state_t:", self.state_t)
            # print(self.state)
            # if self.state_t > self.state_durations[self.episode]:
            if self.state_t == 1500:
                # self.episode += 1
                self.done = True
                self.reset()
                print("##########times_up###########")

        return self.state_t

    def railway_process(self, state):
        # remove the invalid route
        if state == 0:
            for i in range(18):
                for j in range(18):
                    self.pt_env.loc[Signal[i], Signal[j]] = None
            for i in list(All_routes.keys()):
                self.pt_env[int(All_routes[i][0])][int(All_routes[i][1])] = 0

        # 1V60
        if state == 1:
            if self.state_t == self.state_1V60_durations[0]:
                R13(53).on()
                # print("R13:", self.pt_env)
            elif self.state_t == self.state_1V60_durations[1]:
                R24(25).on()
                # print("R24:", self.pt_env)
            elif self.state_t == self.state_1V60_durations[2]:
                R34(11).on()
                # print("R34:", self.pt_env)

        # 1S49
        if state == 2:
            if self.state_t == self.state_1S49_durations[0]:
                R35(9).on()
                # print("R13:", self.pt_env)
            elif self.state_t == self.state_1S49_durations[1]:
                R36(12).on()
                # print("R24:", self.pt_env)
            elif self.state_t == self.state_1S49_durations[2]:
                R32(15).on()
            elif self.state_t == self.state_1S49_durations[3]:
                R30(20).on()
            elif self.state_t == self.state_1S49_durations[4]:
                R17(256).on()
                # print("R17:", self.pt_env)

        # 1V12
        if state == 3:
            if self.state_t == self.state_1V12_durations[0]:
                R13(39).on()
                # print("R13:", self.pt_env)
            elif self.state_t == self.state_1V12_durations[1]:
                R24(25).on()
                # print("R24:", self.pt_env)
            elif self.state_t == self.state_1V12_durations[2]:
                R34(11).on()
                # print("R34:", self.pt_env)

        # 1K69
        if state == 4:
            if self.state_t == self.state_1K69_durations[0]:
                R11(53).on()
                # print(self.state_t)
                # self.state_t += 10
                # print(self.state_t)
                # self.R11_off()
                # print("R13:", self.pt_env)
            elif self.state_t == self.state_1K69_durations[1]:
                R24(25).on()
                # print("R24:", self.pt_env)
            elif self.state_t == self.state_1K69_durations[2]:
                R34(11).on()
                # print("R34:", self.pt_env)

        if state == 5:
            if self.state_t == 1500:
                print("Reset")
        # # 147Q
        # if state == 5:
        #     pass

    def step(self, action):
        global stringstatelist

        if action == 0:  # correct
            if self.state_t == 14:
                self.cur_action = R35(9)
                print("#############R35############:", self.pt_env[Right_signal[1]][Right_signal[2]])
            elif self.state_t == 23:
                self.cur_action = R36(12)
            elif self.state_t == 35:
                self.cur_action = R32(15)
            elif self.state_t == 50:
                self.cur_action = R30(20)
            elif self.state_t == 70:
                self.cur_action = R20(260)
            else:
                Rnochange(1).on()
                self.cur_action = Rnochange(1)

        elif action == 1:
            if self.state_t == 14:
                self.cur_action = R35(9)
                print("#############R35############:", self.pt_env[Right_signal[1]][Right_signal[2]])
            else:
                Rnochange(1).on()
                self.cur_action = Rnochange(1)

        elif action == 2:  # correct
            if self.state_t == 14:
                self.cur_action = R35(9)
                print("#############R35############:", self.pt_env[Right_signal[1]][Right_signal[2]])
            elif self.state_t == 23:
                self.cur_action = R36(12)
            else:
                Rnochange(1).on()
                self.cur_action = Rnochange(1)

        elif action == 3:  # correct
            if self.state_t == 14:
                self.cur_action = R35(9)
                print("#############R35############:", self.pt_env[Right_signal[1]][Right_signal[2]])
            elif self.state_t == 23:
                self.cur_action = R36(12)
            elif self.state_t == 35:
                self.cur_action = R32(15)
            else:
                Rnochange(1).on()
                self.cur_action = Rnochange(1)

        elif action == 4:  # correct
            if self.state_t == 14:
                self.cur_action = R35(9)
                print("#############R35############:", self.pt_env[Right_signal[1]][Right_signal[2]])
            elif self.state_t == 23:
                self.cur_action = R36(12)
            elif self.state_t == 35:
                self.cur_action = R32(15)
            elif self.state_t == 50:
                self.cur_action = R30(20)
            else:
                Rnochange(1).on()
                self.cur_action = Rnochange(1)

        elif action == 5:
            R16(13).on()
            self.cur_action = R16(13)

        elif action == 6:
            R23(25).on()
            self.cur_action = R23(25)

        elif action == 7:
            R24(25).on()
            self.cur_action = R24(25)

        elif action == 8:
            R27(31).on()
            self.cur_action = R27(31)

        elif action == 9:
            R28(31).on()
            self.cur_action = R28(31)

        elif action == 10:
            R33(11).on()
            self.cur_action = R33(11)

        elif action == 11:
            R34(11).on()
            self.cur_action = R34(11)

        elif action == 12:
            R17(256).on()
            self.cur_action = R17(256)
        else:
            pass


        self.conflict = False
        self.done = False
        self.reward = 0  # -867

        # 设置的R一个不能与现在所有车处在的位置冲突 一个不能是自己曾经设置过的位置
        for t1 in trainlist[0:1]:  # 这个循环stringstatelist 是现在所有车的位置
            stringstatelist = []
            for er in t1.statelist:
                stringstatelist.append(er.state[0:3])

        if self.cur_action.state[0:3] in stringstatelist:
            self.conflict = True
            self.done = True
            print("#########conflict#######")
        else:
            self.conflict = False

        if self.conflict == False:

            for t in trainlist[0:1]:

                if t.isfinished:
                    continue
                else:
                    if len(t.statelist) == 0:
                        if len(t.troutelist)!=0 and t.traingaptime == None:
                            self.done = True
                        # 原本长度为0，这次正好开始设置了：
                        # 如果这次设置R的起始点等于列车的开始点，那么就为列车开通路径，并且由于len(t.statelist)==0 说明在这之前车是没在开的
                        if self.cur_action.srs == t.signaltrainstart and (self.cur_action not in t.troutelist):

                            self.pt_env[int(self.cur_action.srs)][int(self.cur_action.sre)] = 1

                            t.train_state(self.cur_action)
                            t.traingaptime = t.statelist[0].gaptime
                            if self.state_t == list(t.planroute.values())[0]:
                                t.trainreward += 100  # 准时地选对了
                            if t.signaltrainstart == list(t.checkpoint.keys())[0]:
                                t.planroute.pop(All_routes[t.statelist[0].state[0:3]][0])
                            t.signaltrainstart = self.cur_action.sre
                            # t.traintime = t.traintime + 1  # 跑起来
                            # t.trainreward += 100
                            print("t_headcode:", t.headcode, t.traintime, t.trainreward, t.traingaptime, t.statelist,
                                  t.planroute, t.troutelist, t.signaltrainstart)
                            self.reward += t.trainreward
                            break

                        else:
                            # 这次R的设置与t无关，并且车没在开
                            t.traintime = 0  # 车没在开
                            if len(list(t.planroute.values())) == 0:
                                self.done = True
                                t.isfinished = True
                            elif self.state_t <= list(t.planroute.values())[0]:  # 如果车还没到预计的点
                                t.trainreward = t.trainreward + 1  # 现在都算是提前的所以没事
                            else:
                                t.trainreward = - 1  # 现在是delay了就直接done
                                print("delay GG!!!")

                    # t.statelist不为0说明已经被安排了
                    else:
                        print("len(t.statelist)：", len(t.statelist))
                        t.traintime = t.traintime + 1

                        # 如果现在的开始等于它路径的下一条那就接着安排
                        if self.cur_action.srs == All_routes[t.statelist[-1].state[0:3]][1]:
                            self.pt_env[int(self.cur_action.srs)][int(self.cur_action.sre)] = 1
                            t.train_state(self.cur_action)
                            # t.trainreward += 100

                        # 列车正好跑到这条路的结尾
                        if t.traintime == t.traingaptime:
                            t.traintime = 0
                            # 如果当前设置

                            self.pt_env[int(t.statelist[0].srs)][int(t.statelist[0].sre)] = 0

                            if All_routes[t.statelist[0].state[0:3]][1] in list(t.checkpoint.keys()):
                                t.planroute.pop(All_routes[t.statelist[0].state[0:3]][1])
                                if self.state_t == t.checkpoint[All_routes[t.statelist[0].state[0:3]][1]]:
                                    # 如果正好是终点 加分！
                                    t.trainreward += 100
                                    if self.state_t == list(t.checkpoint.values())[-1]:
                                        # 如果是这列车的终点 加分
                                        t.trainreward += 100
                                        print(t.headcode + " success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                        # 现在单辆车的情况下就可以done了
                                        self.reward += t.trainreward
                                        self.done = True

                                        if t.headcode == "1K69":
                                            self.done = True
                                            print("done")
                                        t.isfinished = True
                                        break

                            t.statelist = t.statelist[1:]
                            if len(t.statelist) == 0:
                                t.traingaptime = None
                            else:
                                t.traingaptime = t.statelist[0].gaptime
                                t.signaltrainstart = All_routes[t.statelist[0].state[0:3]][1]

                    print("t_headcode:", t.headcode, t.traintime, t.trainreward, t.traingaptime, t.statelist,
                          t.planroute, t.troutelist, t.signaltrainstart)

                    if t.trainreward < 0:
                        self.done = True
                    self.reward += t.trainreward

                    # 如果这列车是第一次被设置 并且设置的route不在列车现在行驶过的路中
                    # if self.cur_action.srs == t.signaltrainstart and (self.cur_action not in t.troutelist):
                    #     if t.traintime == 0:
                    #         t.train_state(self.cur_action)
                    #         t.signaltrainstart = self.cur_action.sre
                    #         t.traintime = t.traintime + 1
                    #
                    #         if self.state_t == list(t.checkpoint.values())[0]:
                    #             t.trainreward += 1000   #准时地选对了
                    #         elif All_routes[t.statelist[0].state[0:3]][0] in list(t.checkpoint.keys()):
                    #             if self.state_t <= t.checkpoint[All_routes[t.statelist[0].state[0:3]][0]]:
                    #                 t.trainreward = t.trainreward + 1
                    #             else:
                    #                 t.trainreward = - 1
                    #         print("t_headcode:", t.headcode, t.traintime, t.trainreward, t.traingaptime, t.statelist )
                    #         break
                    #
                    #
                    # elif len(t.statelist) != 0:
                    #     print("len(t.statelist)：", len(t.statelist))
                    #     t.traintime = t.traintime + 1
                    #
                    #     if t.traintime  == t.traingaptime:
                    #         t.traintime = 0
                    #
                    #         if All_routes[t.statelist[0].state[0:3]][1] in list(t.checkpoint.keys()):
                    #             if self.state_t == t.checkpoint[All_routes[t.statelist[0].state[0:3]][1]]:
                    #                 t.trainreward += 1000
                    #                 # t.trainreward = -abs(self.state_t - t.checkpoint[All_routes[t.statelist[0].state[0:3]][1]])
                    #                 # if t.traintime == t.traingaptime and (All_routes[t.statelist[0].state[0:3]][1] == list(t.checkpoint.keys())[-1]):
                    #                 if self.state_t == list(t.checkpoint.values())[-1]:
                    #                     t.trainreward += 1000
                    #                     print(t.headcode + " success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    #                     if t.headcode == "1K69":
                    #                         self.done = True
                    #                         print("done")
                    #                     t.isfinished = True
                    #         t.statelist = t.statelist[1:]
                    #
                    #     elif self.cur_action.srs == All_routes[t.statelist[-1].state[0:3]][0]:
                    #         t.train_state(self.cur_action)
                    #         print("t_headcode:", t.headcode, t.traintime, t.trainreward, t.traingaptime, t.statelist )
                    # # elif self.state_t == 1500:
                    # #     self.done = True
                    # else:
                    #     t.traintime = 0
                    #     if len(t.troutelist) == 0:
                    #         if self.state_t <= list(t.checkpoint.values())[0]:
                    #             t.trainreward = t.trainreward + 1
                    #         else:
                    #             t.trainreward = - 1
                    #
                    # print("t_headcode:", t.headcode, t.traintime, t.trainreward, t.traingaptime, t.statelist )
                    #
                    # if t.trainreward < 0:
                    #     self.done = True
                    #
                    # self.reward += t.trainreward

        self.info = []

        self.R11_condition = self.pt_env[Left_signal[7]][Left_signal[4]]
        self.R12_condition = self.pt_env[Left_signal[7]][Left_signal[3]]
        self.R13_condition = self.pt_env[Left_signal[6]][Left_signal[4]]
        self.R14_condition = self.pt_env[Left_signal[6]][Left_signal[3]]
        self.R15_condition = self.pt_env[Left_signal[5]][Left_signal[4]]
        self.R16_condition = self.pt_env[Left_signal[5]][Left_signal[3]]
        self.R17_condition = self.pt_env[Right_signal[5]][Right_signal[6]]
        self.R18_condition = self.pt_env[Right_signal[5]][Right_signal[7]]
        self.R19_condition = self.pt_env[Right_signal[5]][Right_signal[8]]
        self.R20_condition = self.pt_env[Right_signal[5]][Right_signal[9]]
        # R21，R22不存在
        self.R23_condition = self.pt_env[Left_signal[4]][Left_signal[2]]
        self.R24_condition = self.pt_env[Left_signal[4]][Left_signal[1]]
        # R25/26 上面不存在
        self.R27_condition = self.pt_env[Left_signal[3]][Left_signal[2]]
        self.R28_condition = self.pt_env[Left_signal[3]][Left_signal[1]]
        self.R29_condition = self.pt_env[Right_signal[4]][Right_signal[5]]
        self.R30_condition = self.pt_env[Right_signal[3]][Right_signal[5]]
        self.R31_condition = self.pt_env[Right_signal[2]][Right_signal[4]]
        self.R32_condition = self.pt_env[Right_signal[2]][Right_signal[3]]
        self.R33_condition = self.pt_env[Left_signal[2]][Left_signal[0]]
        self.R34_condition = self.pt_env[Left_signal[2]][Left_signal[0]]
        self.R35_condition = self.pt_env[Right_signal[1]][Right_signal[2]]
        self.R36_condition = self.pt_env[Right_signal[0]][Right_signal[1]]
        self.obs = [self.R11_condition,
                    self.R12_condition,
                    self.R13_condition,
                    self.R14_condition,
                    self.R15_condition,
                    self.R16_condition,
                    self.R17_condition,
                    self.R18_condition,
                    self.R19_condition,
                    self.R20_condition,
                    self.R23_condition,
                    self.R24_condition,
                    self.R27_condition,
                    self.R28_condition,
                    self.R29_condition,
                    self.R30_condition,
                    self.R31_condition,
                    self.R32_condition,
                    self.R33_condition,
                    self.R34_condition,
                    self.R35_condition,
                    self.R36_condition,
                    t1M99.traintime,
                    t1V60.traintime,
                    t1K69.traintime,
                    t1V12.traintime,
                    t1S49.traintime,
                    self.state_t]
        print(self.obs)

        return np.array(self.obs).astype(np.float32), self.reward, self.done, self.info

    def reset(self):
        # self.timeStep = 1
        # self.episode = 0
        self.last_state = 0
        self.state_t = 0
        self.reward = 0
        self.state_durations = [25, 95, 455, 755, 1340, 1500]
        self.state_2N57_durations = []
        self.state_1V60_durations = [30, 69, 94]
        self.state_1S49_durations = [394, 403, 415, 430, 450]
        self.state_1V12_durations = [700, 729, 754]
        self.state_1K69_durations = [1260, 1312, 1336]

        self.Peartree_env = np.zeros((18, 18), dtype=np.int64)
        self.pt_env = pd.DataFrame(self.Peartree_env, index=Signal,
                                   columns=Signal)

        for i in range(18):
            for j in range(18):
                self.pt_env.loc[Signal[i], Signal[j]] = None
        for i in list(All_routes.keys()):
            self.pt_env[int(All_routes[i][0])][int(All_routes[i][1])] = 0

        observation = [self.R11_condition,
                       self.R12_condition,
                       self.R13_condition,
                       self.R14_condition,
                       self.R15_condition,
                       self.R16_condition,
                       self.R17_condition,
                       self.R18_condition,
                       self.R19_condition,
                       self.R20_condition,
                       self.R23_condition,
                       self.R24_condition,
                       self.R27_condition,
                       self.R28_condition,
                       self.R29_condition,
                       self.R30_condition,
                       self.R31_condition,
                       self.R32_condition,
                       self.R33_condition,
                       self.R34_condition,
                       self.R35_condition,
                       self.R36_condition,
                       t1M99.traintime,
                       t1V60.traintime,
                       t1K69.traintime,
                       t1V12.traintime,
                       t1S49.traintime,
                       self.state_t]

        for t in trainlist:
            t.treset()

        return np.array(observation).astype(np.float32)


class R11(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R11_on'
        self.gaptime = gaptime
        self.srs = All_routes['R11'][0]
        self.sre = All_routes['R11'][1]

    def on(self):
        self.pt_env[Left_signal[7]][Left_signal[4]] = 1
        global r11ontime
        r11ontime = self.state_t

        if self.state_t == r11ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[7]][Left_signal[4]] = 0
        self.state = 'R11_off'


class R12(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R12_on'
        self.gaptime = gaptime
        self.srs = All_routes['R12'][0]
        self.sre = All_routes['R12'][1]

    def on(self):
        self.pt_env[Left_signal[7]][Left_signal[3]] = 1
        global r12ontime
        r12ontime = self.state_t
        if self.state_t == r12ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[7]][Left_signal[3]] = 0
        self.state = 'R12_off'


class R13(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R13_on'  # 默认状态为'R13_on
        self.gaptime = gaptime
        self.srs = All_routes['R13'][0]
        self.sre = All_routes['R13'][1]

    def on(self):
        self.pt_env[Left_signal[6]][Left_signal[4]] = 1
        global r13ontime
        r13ontime = self.state_t
        if self.state_t == r13ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[6]][Left_signal[4]] = 0
        self.state = 'R13_off'


# R12


class R14(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R14_on'  # 默认状态为'R14_on
        self.gaptime = gaptime
        self.srs = All_routes['R14'][0]
        self.sre = All_routes['R14'][1]

    def on(self):
        self.pt_env[Left_signal[6]][Left_signal[3]] = 1
        global r14ontime
        r14ontime = self.state_t
        if self.state_t == r14ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[6]][Left_signal[3]] = 0
        self.state = 'R14_off'


class R15(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R15_on'  # 默认状态为'R15_on
        self.gaptime = gaptime
        self.srs = All_routes['R15'][0]
        self.sre = All_routes['R15'][1]

    def on(self):
        self.pt_env[Left_signal[5]][Left_signal[4]] = 1
        global r15ontime
        r15ontime = self.state_t
        if self.state_t == r15ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[5]][Left_signal[4]] = 0
        self.state = 'R15_off'


class R16(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R16_on'  # 默认状态为'R16_on
        self.gaptime = gaptime
        self.srs = All_routes['R16'][0]
        self.sre = All_routes['R16'][1]

    def on(self):
        self.pt_env[Left_signal[5]][Left_signal[3]] = 1
        global r16ontime
        r16ontime = self.state_t
        if self.state_t == r16ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[5]][Left_signal[3]] = 0
        self.state = 'R16_off'


class R23(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R23_on'  # 默认状态为'R23_on
        self.gaptime = gaptime
        self.srs = All_routes['R23'][0]
        self.sre = All_routes['R23'][1]

    def on(self):
        self.pt_env[Left_signal[4]][Left_signal[2]] = 1
        global r23ontime
        r23ontime = self.state_t
        if self.state_t == r23ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[4]][Left_signal[2]] = 0
        self.state = 'R23_off'


class R24(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R24_on'  # 默认状态为'R24_on
        self.gaptime = gaptime
        self.srs = All_routes['R24'][0]
        self.sre = All_routes['R24'][1]

    def on(self):
        self.pt_env[Left_signal[4]][Left_signal[1]] = 1
        global r24ontime
        r24ontime = self.state_t
        if self.state_t == r24ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[4]][Left_signal[1]] = 0
        self.state = 'R24_off'


# def R26(self):  ###### have a problem ###
#     self.Peartree.pt_env[self.left_signal[3]][self.left_signal[4]] = 1

class R27(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R27_on'  # 默认状态为'R27_on
        self.gaptime = gaptime
        self.srs = All_routes['R27'][0]
        self.sre = All_routes['R27'][1]

    def on(self):
        self.pt_env[Left_signal[3]][Left_signal[2]] = 1
        global r27ontime
        r27ontime = self.state_t
        if self.state_t == r27ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[3]][Left_signal[2]] = 0
        self.state = 'R27_off'


class R28(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R28_on'  # 默认状态为'R28_on
        self.gaptime = gaptime
        self.srs = All_routes['R28'][0]
        self.sre = All_routes['R28'][1]

    def on(self):
        self.pt_env[Left_signal[3]][Left_signal[1]] = 1
        global r28ontime
        r28ontime = self.state_t
        if self.state_t == r28ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[3]][Left_signal[1]] = 0
        self.state = 'R28_off'


class R33(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R33_on'  # 默认状态为'R33_on
        self.gaptime = gaptime
        self.srs = All_routes['R33'][0]
        self.sre = All_routes['R33'][1]

    def on(self):
        self.pt_env[Left_signal[2]][Left_signal[0]] = 1
        global r33ontime
        r33ontime = self.state_t
        if self.state_t == r33ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[2]][Left_signal[0]] = 0
        self.state = 'R33_off'


class R34(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R34_on'  # 默认状态为'R34_on
        self.gaptime = gaptime
        self.srs = All_routes['R34'][0]
        self.sre = All_routes['R34'][1]

    def on(self):
        self.pt_env[Left_signal[1]][Left_signal[0]] = 1
        global r34ontime
        r34ontime = self.state_t
        if self.state_t == r34ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Left_signal[1]][Left_signal[0]] = 0
        self.state = 'R34_off'


class R17(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R17_on'  # 默认状态为'R17_on
        self.gaptime = gaptime
        self.srs = All_routes['R17'][0]
        self.sre = All_routes['R17'][1]

    def on(self):
        self.pt_env[Right_signal[5]][Right_signal[6]] = 1
        global r17ontime
        r17ontime = self.state_t
        if self.state_t == r17ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[5]][Right_signal[6]] = 0
        self.state = 'R17_off'


class R18(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R18_on'  # 默认状态为'R18_on
        self.gaptime = gaptime
        self.srs = All_routes['R18'][0]
        self.sre = All_routes['R18'][1]

    def on(self):
        self.pt_env[Right_signal[5]][Right_signal[7]] = 1
        global r18ontime
        r18ontime = self.state_t
        if self.state_t == r18ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[5]][Right_signal[7]] = 0
        self.state = 'R18_off'


class R19(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R19_on'  # 默认状态为'R19_on
        self.gaptime = gaptime
        self.srs = All_routes['R19'][0]
        self.sre = All_routes['R19'][1]

    def on(self):
        self.pt_env[Right_signal[5]][Right_signal[8]] = 1
        # self.pt_env[Right_signal[5]][Right_signal[9]] = 1 #为啥是两个?
        global r19ontime
        r19ontime = self.state_t
        if self.state_t == r19ontime + self.gaptime:  # 这边改gap time 就行了  你模仿下面的R20  只要在on里写就行了
            self.off()

    def off(self):
        self.pt_env[Right_signal[5]][Right_signal[8]] = 0
        self.state = 'R19_off'


class R20(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R20_on'  # 默认状态为'R20_on
        self.gaptime = gaptime
        self.srs = All_routes['R20'][0]
        self.sre = All_routes['R20'][1]

    def on(self):
        self.pt_env[Right_signal[5]][Right_signal[9]] = 1
        global r20ontime
        r20ontime = self.state_t
        if self.state_t == r20ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[5]][Right_signal[9]] = 0
        self.state = 'R20_off'


class R29(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R29_on'  # 默认状态为'R29_on
        self.gaptime = gaptime
        self.srs = All_routes['R29'][0]
        self.sre = All_routes['R29'][1]

    def on(self):
        self.pt_env[Right_signal[4]][Right_signal[5]] = 1
        global r29ontime
        r29ontime = self.state_t
        if self.state_t == r29ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[4]][Right_signal[5]] = 0
        self.state = 'R29_off'


class R30(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R30_on'  # 默认状态为'R19_on
        self.gaptime = gaptime
        self.srs = All_routes['R30'][0]
        self.sre = All_routes['R30'][1]

    def on(self):
        self.pt_env[Right_signal[3]][Right_signal[5]] = 1
        global r30ontime
        r30ontime = self.state_t
        if self.state_t == r30ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[3]][Right_signal[5]] = 0
        self.state = 'R30_off'


class R31(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R31_on'  # 默认状态为'R31_on
        self.gaptime = gaptime
        self.srs = All_routes['R31'][0]
        self.sre = All_routes['R31'][1]

    def on(self):
        self.pt_env[Right_signal[2]][Right_signal[4]] = 1
        global r31ontime
        r31ontime = self.state_t
        if self.state_t == r31ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[2]][Right_signal[4]] = 0
        self.state = 'R31_off'


class R32(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R32_on'  # 默认状态为'R32_on
        self.gaptime = gaptime
        self.srs = All_routes['R32'][0]
        self.sre = All_routes['R32'][1]

    def on(self):
        self.pt_env[Right_signal[2]][Right_signal[3]] = 1
        global r32ontime
        r32ontime = self.state_t
        if self.state_t == r32ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[2]][Right_signal[3]] = 0
        self.state = 'R32_off'


class R35(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R35_on'  # 默认状态为'R35_on
        self.gaptime = gaptime
        self.srs = All_routes['R35'][0]
        self.sre = All_routes['R35'][1]

    def on(self):
        self.pt_env[Right_signal[1]][Right_signal[2]] = 1
        global r35ontime
        r35ontime = self.state_t
        if self.state_t == r35ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[1]][Right_signal[2]] = 0
        self.state = 'R35_off'


class R36(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'R36_on'  # 默认状态为'R36_on
        self.gaptime = gaptime
        self.srs = All_routes['R36'][0]
        self.sre = All_routes['R36'][1]

    def on(self):
        self.pt_env[Right_signal[0]][Right_signal[1]] = 1
        global r36ontime
        r36ontime = self.state_t
        if self.state_t == r36ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env[Right_signal[0]][Right_signal[1]] = 0
        self.state = 'R36_off'


class Rnochange(PeartreeEnv):
    def __init__(self, gaptime):
        super().__init__()
        self.state = 'Rnochange'  # 默认状态为'R36_on
        self.gaptime = 1
        self.srs = ''
        self.sre = ''

    def on(self):
        self.pt_env = self.pt_env
        global r36ontime
        r36ontime = self.state_t
        if self.state_t == r36ontime + self.gaptime:
            self.off()

    def off(self):
        self.pt_env = self.pt_env
        self.state = 'R36_off'


if __name__ == "__main__":
    env = PeartreeEnv()

    for i in range(5):
        print("i:", i)
        env.reset()

        done = False
        while not done:
            env.update_time()
            # action = env.action_space.sample()
            action = 2
            print(action)

            # print("step:", step)
            # print("action:", action)
            # print(self.state_t)
            obs, reward, info, done = env.step(action)
            print("reward:", reward)
            # if done is True:
            #     self.reset()

            # self.no_name()
            # env.railway_process(env.state)
            if env.state_t == 1500:
                done = True
                env.reset()

# if __name__ == "__main__":
#     env = PeartreeEnv()
#     env.reset()
#
#
#     def time_in_env(self):
#         # while True:
#         for step in range(5000):
#             self.update_time()
#
#             # action = self.action_space.sample()
#             action = 2
#             print("step:", step)
#             print("action:", action)
#             # print("state_t:", self.state_t)
#             obs, reward, info, done = self.step(action)
#             # print("reward:", reward)
#             if done is True:
#                 self.reset()
#                 print("env_reset")
#
#             # self.no_name()
#             # self.railway_process(self.state)
#             # if self.state == 6:
#             #     break
#             if self.state_t == 1500:
#                 self.reset()
#                 # print("time_reset")
#                 # print("time_update")
#
#
#     time_in_env(env)
