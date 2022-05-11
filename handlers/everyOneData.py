
import _pickle as cPickle
import os.path

class EveryOneData:
    DataFileName = "EveryOneBot.data"
    def __init__(self):
        self.names = []
        self.ids = []

        self.DATA_SAVE = {
            "names" : self.names,
            "ids"  : self.ids
        }

        try:
            self.loadEveryone()
        except:
            self.saveEveryOne()

    def addUser(self, from_user):
        userId = from_user.id
        if from_user.username:
            name = from_user.username
        else:
            name = from_user.first_name
        if userId in self.ids:
            id_index = self.ids.index(userId)
            self.names[id_index] = name
        else:
            self.names.append(name)
            self.ids.append(userId)
        self.saveEveryOne()
        return

    def saveEveryOne(self):
        with open(EveryOneData.DataFileName, "wb") as f:
            cPickle.dump(self.DATA_SAVE, f)

    def loadEveryone(self):
        with open(EveryOneData.DataFileName, "rb") as f:
            self.DATA_SAVE = cPickle.load(f)
            for key in self.DATA_SAVE:
                self.__setattr__(key, self.DATA_SAVE[key])

    def getEveryoneNames(self):
        resNames = ', '.join(list(map(lambda name:f"@{name}", self.names)))
        return resNames

    def getEveryoneChatIds(self):
        return self.ids
