import numpy as np
import math
from each_train import *

# ====== Action choice ======#
# env = PeartreeEnv()

t1V60 = t1V60()
t1S49 = t1S49()
t1V12 = t1V12()
t1K69 = t1K69()
t1M99 = t1M99()

Right_Action = ["R17", "R18", "R19", "R20", "R25", "R29", "R30", "R31", "R32", "R35", "R36"]
Right_signal = [5332, 5330, 5328, 5324, 5322, 5316, 5300, 5304, 5306, 5308]
RS_L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10
RS_H = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 10

Left_Action = ["R11", "R12", "R13", "R14", "R15", "R16", "R23", "R24", "R26", "R27", "R28", "R33", "R34"]
Left_signal = [5333, 5331, 5329, 5321, 5319, 5315, 5313, 5311]
LS_L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 12
LS_H = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 12
Low_traintime = [0, 0, 0, 0, 0, 0]
High_traintime = [300, 300, 300, 300, 300, 1500]
Low = np.append(RS_L, LS_L)
High = np.append(RS_H, LS_H)
Low_ = np.append(Low, Low_traintime)
High_ = np.append(High, High_traintime)

Actions = np.append(Right_Action, Left_Action)
Direction = ["Start", "End"]



# print(Actions)
# ====== Signal ======#
Actions_list = ['r17', 'r18', 'r19', 'r20', 'r29', 'r30', 'r31', 'r32',
                'r35', 'r36', 'r11', 'r12', 'r13', 'r14', 'r15', 'r16',
                'r23', 'r24', 'r27', 'r28', 'r33', 'r34']

Signal = np.append(Right_signal, Left_signal)

# ====== Routes ======#
All_routes = {'R11': ('5311', '5319'),  #0
              'R12': ('5311', '5321'),  #1
              'R13': ('5313', '5319'),  #2
              'R14': ('5313', '5321'),  #3
              'R15': ('5315', '5319'),  #4
              'R16': ('5315', '5321'),  #5
              'R17': ('5316', '5300'),  #12
              'R18': ('5316', '5304'),  #13
              'R19': ('5316', '5306'),  #14
              'R20': ('5316', '5308'),  #15
              'R23': ('5319', '5329'),  #6
              'R24': ('5319', '5331'),  #7
              # 'R25': ('5320', '5318'),
              # 'R26': ('5321', '5323'),
              'R27': ('5321', '5329'),  #8
              'R28': ('5321', '5331'),  #9
              'R29': ('5322', '5316'),  #16
              'R30': ('5324', '5316'),  #17
              'R31': ('5328', '5322'),  #18
              'R32': ('5328', '5324'),  #19
              'R33': ('5329', '5333'),  #10
              'R34': ('5331', '5333'),  #11
              'R35': ('5332', '5330'),  #20
              'R36': ('5330', '5328')}  #21

# ====== TIME ======#
start_time = (2023, 4, 4, 15, 29, 0, 1, 94, 0)
end_time = (start_time[0], start_time[1], start_time[2], start_time[3], start_time[4], start_time[5], start_time[6],
            start_time[7], start_time[8])

# ====== observation ======#


# ====== Trainlist ===== #
trainlist = [t1M99 ,t1V60, t1S49, t1V12, t1K69, ]
Train_start = [ "5332","5313", "5332", "5313", "5311"]
Train_end = ["5308","5333", "5300", "5333", "5333" ]
