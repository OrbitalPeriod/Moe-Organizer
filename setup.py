import json
from os import makedirs
from utils import folders
import sqlite3

def main():
    createFolders()
    createDatabase()
    pass

def createFolders():
    
    try:
        makedirs(folders.getImportFolder())
    except FileExistsError:
        pass
    try:
        makedirs(folders.getLongTermStorage())
    except FileExistsError:
        pass
    try:
        makedirs(folders.getShortTermStorage())
    except FileExistsError:
        pass
    try:
        makedirs(folders.getImportFolder())
    except FileExistsError:
        pass
    
def createDatabase():
    con = sqlite3.connect(folders.getDBLocation())
    cur = con.cursor()

    cur.execute("CREATE TABLE taglist (imageID, tag)")
    cur.execute("CREATE TABLE imagelist (imageID, filename, imagehash)")
    cur.execute("CREATE TABLE pixivids (pixivID)")

    con.commit()
    con.close()

    pass

def createConfigFile():
    json_dict = {}
    json_dict["pixiv"] = ""
    json_dict["pixivUID"] = ""
    json_dict["twitter"] = ""
    json_dict["saucenao"] = ""
    json_dict["gelbooru_key"] = ""
    json_dict["gelbooru_user"] = ""
    json_dict["long term storage dir"] = "storage//long_term"
    json_dict["short term storage dir"] = "storage//short_term"
    json_dict["unsuported formats dir"] = "storage//other_formats"
    json_dict["import folder"] = "storage//import"
    json_dict["database"] = "storage/database.db"

    with open("config.json", "w") as fp:
        json.dump(json_dict, fp, indent=6)


if __name__ == "__main__":
    main()