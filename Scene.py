class Scene:
    def init(self, name, desc):
        self.name = name
        self.desc = desc

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def setName(self, name):
        self.name = name

    def setDesc(self, desc):
        self.desc = desc