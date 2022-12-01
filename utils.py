import json

class keys:
    def getSaucenaokey():
        with open("config.json") as f:
            data = json.load(f)
            return data["saucenao"]
    def getTwitterkey():
        with open("config.json") as f:
            data = json.load(f)
            return data["twitter"]
    def getPixivkey():
        with open("config.json") as f:
            data = json.load(f)
        return data["pixiv"]
class folders:
    def getLongTermStorage():
        with open("config.json") as f:
            data = json.load(f)
        return data["long term storage dir"]
    def getImportFolder():
        with open("config.json") as f:
            data = json.load(f)
        return data["import folder"]
    def getShortTermStorage():
        with open("config.json") as f:
            data = json.load(f)
        return data["short term storage dir"]
    
    


