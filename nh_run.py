from All_route import *
from each_train import *
from Peartree_env_v7 import *

if __name__ == "__main__":
    env = PeartreeEnv()
    r11 = R11(53)
    r12 = R12(27)
    r13 = R13(39)
    r14 = R14(31)
    r15 = R15(21)
    r16 = R16(13)
    r23 = R23(25)
    r24 = R24(25)
    r27 = R27(31)
    r28 = R28(31)
    r33 = R33(11)
    r34 = R34(11)
    r17 = R17(256)
    r18 = R18(250)
    r19 = R19(251)
    r20 = R20(260)
    r29 = R29(23)
    r30 = R30(20)
    r31 = R31(36)
    r32 = R32(15)
    r35 = R35(9)
    r36 = R36(12)
    t1V60 = t1V60()
    t1S49 = t1S49()
    t1V12 = t1V12()
    t1K69 = t1K69()
    t1M99 = t1M99()
    Actions_list = [r17, r18, r19, r20, r29, r30, r31, r32, r35, r36, r11, r12, r13, r14, r15, r16, r23, r24, r27, r28,
                    r33, r34]
    trainlist = [t1V60, t1S49, t1V12, t1K69, t1M99]
    conflict = False

    reward = 0
    for step in range(5000):
        env.state_t = env.state_t + 1

        random_index = random.randint(0, len(Actions_list) - 1)
        cur_action = Actions_list[random_index]

        for t1 in trainlist:
            if cur_action.state in t1.state:
                conflict = True
            else:
                conflict = False

        if conflict == False:
            for t in trainlist:
                # 如果这列车是第一次被设置
                if cur_action.srs == t.signaltrainstart:
                    if t.traintime == 0:
                        t.state.append(cur_action.state)
                        t.signaltrainstart = cur_action.sre
                        t.traintime = t.traintime + 1

                elif len(t.state) != 0:
                    t.traintime = t.traintime + 1
                    if t.traintime == t.traingaptime and All_routes[t.state[0][0:3]][1] in list(t.checkpoint.keys()):
                        t.trainreward = -abs(env.state_t - t.checkpoint[All_routes[t.state[0][0:3]][1]])
                        t.traintime = 0
                        t.state = t.state[1:]
                    elif t.traintime == t.traingaptime:
                        t.traintime = 0
                        t.state = t.state[1:]
                else:
                    t.traintime = 0
                reward = reward + t.trainreward
        else:

            for t in trainlist:
                if t.traintime == 0:
                    break
                else:
                    t.traintime = t.traintime + 1
                    if t.traintime == t.traingaptime and All_routes[t.state[0][0:3]][1] in list(t.checkpoint.keys()):
                        t.trainreward = -abs(env.state_t - t.checkpoint[All_routes[t.state[0][0:3]][1]])
                        t.traintime = 0
                        t.state = t.state[1:]

                reward = reward + t.trainreward
        print(reward)
