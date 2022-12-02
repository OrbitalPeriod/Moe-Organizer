import utils

import sqlite3

def getCon():
    return sqlite3.connect(utils.folders.getDBLocation())

def setup():
    con = getCon()
    cur = con.cursor()
    cur.execute("CREATE TABLE taglist(imageID, tag)")
    cur.execute("CREATE TABLE imagelist(imageID, filename)")
    res = cur.execute("SELECT name FROM sqlite_master")
    print(res.fetchall())
    con.commit()
    con.close()

def importImage(imageID, filename, hash):
    con = getCon()
    cur = con.cursor()

    data = (str(imageID), filename, str(hash))
    cur.execute("INSERT INTO imagelist VALUES (?, ?, ?)", data)

    con.commit()
    con.close()

def addTag(imageID, tagList):
    con = getCon()
    cur = con.cursor()

    data = []
    for i in range(0, len(tagList)):
        data.append((str(imageID), tagList[i]))

    cur.executemany("INSERT INTO taglist VALUES(?, ?)", data)

    con.commit()
    con.close()

def getFile(imageID):
    con = getCon()
    cur = con.cursor()

    cur.execute(f"SELECT filename FROM imagelist WHERE imageID='{imageID}'")
    filepath = cur.fetchone()[0]
    con.close()
    return filepath

def getImageID(tag):
    con = getCon()
    cur = con.cursor()

    cur.execute(f"SELECT imageID FROM taglist WHERE tag='{tag}'")
    imageID = cur.fetchall()
    con.close()

    imageIDs = []
    for i in range(0, len(imageID)):
        imageIDs.append(imageID[i][0])

    return imageIDs

def getmaxID():
    con = getCon()
    cur = con.cursor()

    cur.execute('SELECT MAX(imageID) as max_ID FROM imagelist;')
    res = cur.fetchone()[0]
    if res == None:
        return 0
    else:
        return res

def chechHash(hash):        #return false if it doesnt exist
    con = getCon()
    cur = con.cursor()

    cur.execute(f"SELECT * FROM imagelist WHERE hash='{hash}'")
    result = cur.fetchone()

    if result == None:
        return False
    else:
        return True

def checkPixivID(id):   #return false if it doesnt exist
    con = getCon()
    cur = con.cursor()

    cur.execute(f"SELECT * FROM pixivids WHERE pixivID='{id}'")
    result = cur.fetchone()
    if result == None:
        return False
    else:
        return True
def addpixivID(id):
    con = getCon()
    cur = con.cursor()

    cur.execute(f"INSERT INTO pixivids VALUES ({id})")

    con.commit()
    con.close()

def topTags():
    con = getCon()
    cur = con.cursor()

    cur.execute(f'SELECT tag FROM taglist')
    results = cur.fetchall()

    counting_dict = {}
    for result in results:
        if result[0] in counting_dict:
            counting_dict[result[0]] = counting_dict[result[0]] + 1
        else:
            counting_dict[result[0]] = 1
    
    organized = sorted(counting_dict.items(), key= lambda x: x[1], reverse=True)

    return organized