
import _pickle as cPickle
import os.path

class EveryOneData:
    DataFileName  = "EveryOneBot.data"
    FlagsFileName = "EveryOneBot.flags"
    def __init__(self):
        self.names = []
        self.ids = []

        self.DATA_SAVE = {
            "names" : self.names,
            "ids"  : self.ids
        }

        self.userFlags = {
            # id : []
        }

        try:
            self.loadEveryone()
        except:
            self.saveEveryOne()


        try:
            self.loadFlags()
        except:
            self.saveFlags()

    def updateDefaultFlags(self):
        for id in self.ids:
            self.updateDefaultFlag(id)

    def updateDefaultFlag(self, id):
        if id not in self.userFlags.keys():
            self.userFlags[id] = self.getDefaultFlags()

    def loadFlags(self):
        with open(EveryOneData.FlagsFileName, "rb") as f:
            self.userFlags = cPickle.load(f)

    def saveFlags(self):
        self.updateDefaultFlags()
        with open(EveryOneData.FlagsFileName, "wb") as f:
            cPickle.dump(self.userFlags, f)

    def is_userWontMessages(self, from_user):
        userId = from_user.id
        self.updateDefaultFlag(userId)
        return self.userFlags[userId][0]

    def userWontMessages(self, from_user, f_status):
        userId = from_user.id
        self.updateDefaultFlag(userId)
        self.userFlags[userId][0] = f_status

    #[Personal message, ]
    def getDefaultFlags(self):
        return [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    def getName(self, from_user):
        if from_user.username:
            name = from_user.username
        else:
            name = from_user.first_name
        return name

    def removeUser(self, from_user):
        userId = from_user.id
        if userId in self.ids:
            id_index = self.ids.index(userId)
            self.names[id_index], self.names[-1] = self.names[-1], self.names[id_index]
            self.ids[id_index], self.ids[-1] = self.ids[-1], self.ids[id_index]
            del self.names[id_index]
            del self.ids[id_index]
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
