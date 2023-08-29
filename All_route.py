from Peartree_env_v7 import PeartreeEnv
from constants import *

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

# 创建R12对象


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

# 创建R14对象


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

# 创建R15对象


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

# 创建R16对象


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

# 创建R23对象


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

# 创建R24对象


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

# 创建R27对象


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

# 创建R28对象


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

# 创建R33对象


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

# 创建R28对象


# To right

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

# 创建R17对象


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

# 创建R18对象


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

# 创建R19对象


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

# 创建R20对象


# def R25(self): # 5320 - 5318
#     pass

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

# 创建R29对象


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

# 创建R30对象


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

# 创建R30对象


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

# 创建R30对象


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

# 创建R35对象


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

# r11 = R11(53)
# r12 = R12(27)
# r13 = R13(39)
# r14 = R14(31)
# r15 = R15(21)
# r16 = R16(13)
# r23 = R23(25)
# r24 = R24(25)
# r27 = R27(31)
# r28 = R28(31)
# r33 = R33(11)
# r34 = R34(11)
# r17 = R17(256)
# r18 = R18(250)
# r19 = R19(251)
# r20 = R20(260)
# r29 = R29(23)
# r30 = R30(20)
# r31 = R31(36)
# r32 = R32(15)
# r35 = R35(9)
# r36 = R36(12)