import json

class ConfigReader:
    def __init__(self):
        self.allConfig = {}
        self.baseUrl = "Config\\"
        listConfig = json.load(open("D:\\P2_1\\Config\\jsonList.json"))
        self.readAllConfig(listConfig)

    def readAllConfig(self, listConfig):
        for fileName in listConfig:
            self.readJsonConfigFile(fileName)
#         print(self.allConfig)

    def readJsonConfigFile(self, fileName):
        jsonConfig = json.load(open("D:\\P2_1\\Config\\" + fileName))
        self.allConfig[fileName] = jsonConfig

    #============= DEF FUNC HERE ============
    
    def getConfigByName(self, fName):
        return self.allConfig[fName]
    
    def getConfigByElement(self, fName, eName):
        return self.getConfigByName(fName)[eName]
    