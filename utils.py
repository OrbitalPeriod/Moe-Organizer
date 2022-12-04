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
    def getGelboorukey():
        with open("config.json") as f:
            data = json.load(f)
        return data["gelbooru_key"]
    def getGelbooruUser():
        with open("config.json") as f:
            data = json.load(f)
        return data["gelbooru_user"]
    def getPixivUID():
        with open("config.json") as f:
            data = json.load(f)
        return data["pixivUID"]
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
    def getDBLocation():
        with open("config.json") as f:
            data = json.load(f)
        return data["database"]
    def getunsuportedStorage():
        with open("config.json") as f:
            data = json.load(f)
        return data["unsuported formats dir"]
    
    


