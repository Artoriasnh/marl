class t1V60():
    def __init__(self):
        super().__init__()
        self.headcode = "1V60"
        self.signaltrainstart = "5313"
        self.signaltrainend = "5333"
        self.statelist = []
        self.troutelist = []   #列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.trainreward = 0
        self.isfinished = False
        self.checkpoint = {'5313':111, '5319': 150, '5331': 175, '5333': 186} #75
        self.planroute = {'5313': 111, '5319': 150, '5331': 175, '5333': 186}  # 75

    def train_state(self, R):
        self.statelist.append(R)
        self.troutelist.append(R)


    def treset(self):
        self.signaltrainstart = "5313"
        self.signaltrainend = "5333"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.planroute = {'5313': 111, '5319': 150, '5331': 175, '5333': 186}  # 75


class t1S49():
    def __init__(self):
        super().__init__()
        self.headcode = "1S49"
        self.signaltrainstart = "5332"
        self.signaltrainend = "5300"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 450
        self.checkpoint = {'5332':258, '5330': 267, '5328': 279, '5324': 294, '5316': 314, '5300': 570} #312
        self.planroute = {'5332': 258, '5330': 267, '5328': 279, '5324': 294, '5316': 314, '5300': 570}  # 312

    def train_state(self, R):
        self.statelist.append(R)
        self.troutelist.append(R)


    def treset(self):
        self.signaltrainstart = "5332"
        self.signaltrainend = "5300"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.planroute = {'5332': 258, '5330': 267, '5328': 279, '5324': 294, '5316': 314, '5300': 570}  # 312


class t1V12():
    def __init__(self):
        super().__init__()
        self.headcode = "1V12"
        self.signaltrainstart = "5313"
        self.signaltrainend = "5333"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.checkpoint = {'5313':771, '5319': 810, '5331': 835, '5333': 846} #75
        self.planroute = {'5313': 771, '5319': 810, '5331': 835, '5333': 846}  # 75

    def train_state(self, R):
        self.statelist.append(R)
        self.troutelist.append(R)


    def treset(self):
        self.signaltrainstart = "5313"
        self.signaltrainend = "5333"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.planroute = {'5313': 771, '5319': 810, '5331': 835, '5333': 846}  # 75


class t1K69():
    def __init__(self):
        super().__init__()
        self.headcode = "1K69"
        self.signaltrainstart = "5311"
        self.signaltrainend = "5333"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.checkpoint = {'5311':1327, '5319': 1380, '5331': 1405, '5333': 1416} #89
        self.planroute = {'5311': 1327, '5319': 1380, '5331': 1405, '5333': 1416}  # 89

    def train_state(self, R):
        self.statelist.append(R)
        self.troutelist.append(R)


    def treset(self):
        self.signaltrainstart = "5311"
        self.signaltrainend = "5333"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.planroute = {'5311': 1327, '5319': 1380, '5331': 1405, '5333': 1416}  # 89


class t1M99():
    def __init__(self):
        super().__init__()
        self.headcode = "1M99"
        self.signaltrainstart = "5332"
        self.signaltrainend = "5308"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.checkpoint = {'5332':14, '5330': 23, '5328': 35, '5324': 50, '5316': 70, '5308': 330}  #316
        self.planroute = {'5332': 14, '5330': 23, '5328': 35, '5324': 50, '5316': 70, '5308': 330}  # 316

    def train_state(self, R):
        self.statelist.append(R)
        self.troutelist.append(R)


    def treset(self):
        self.signaltrainstart = "5332"
        self.signaltrainend = "5308"
        self.statelist = []
        self.troutelist = []  # 列车已经点过那些路径了，点过了就不能再点了
        self.traintime = 0
        self.traingaptime = None
        self.isfinished = False
        self.trainreward = 0
        self.planroute = {'5332': 14, '5330': 23, '5328': 35, '5324': 50, '5316': 70, '5308': 330}  # 316



# t1V60 = t1V60()
# print(list(t1V60.checkpoint.values()))
# print(t1V60.checkpoint)
# t1V60.checkpoint.pop('5313')
# print(t1V60.checkpoint)
# print(len(t1V60.statelist))
# t1S49 = t1S49()
# t1V12 = t1V12()
# t1K69 = t1K69()
# t1M99 = t1M99()
