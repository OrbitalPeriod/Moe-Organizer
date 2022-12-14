import utils
import database
from saucehandler import saucehandler
import asyncio
from os import listdir, remove, rename
import shutil
import time
from PIL import Image
import imagehash
from imagefetcher import PixivFetcher
import threading
from http_server import run_server

async def tagLoop():
    sauce = saucehandler()
    oldFilePath = ""
    PernamentFilePath = ""

    print("Tagloop started")

    while True:
        files = listdir(utils.folders.getShortTermStorage())
        for file in files:
            if ".jpeg" in file:
                rename(utils.folders.getShortTermStorage() + "//" + file, utils.folders.getShortTermStorage() + "//" + file.split(".")[0] + ".png")
                file = file.split(".")[0] + ".png"
            elif ".jpg" in file:
                rename(utils.folders.getShortTermStorage() + "//" + file, utils.folders.getShortTermStorage() + "//" + file.split(".")[0] + ".png")
                file = file.split(".")[0] + ".png"
            elif ".png" not in file:
                shutil.move(utils.folders.getShortTermStorage() + "//" + file, utils.folders.getunsuportedStorage() + "//" + file)
                continue

            oldFilePath = utils.folders.getShortTermStorage() + "//" + file
            imageID = int(database.getmaxID()) + 1
            PernamentFilePath = utils.folders.getLongTermStorage() + "//" + str(imageID) + ".png"

            data = await sauce.processFile(file)

            hash = imagehash.average_hash(Image.open(oldFilePath))

            if not database.chechHash(hash):
                database.addTag(imageID, data[1])
                database.importImage(imageID, PernamentFilePath, hash)
                shutil.move(oldFilePath, PernamentFilePath)
            else:
                remove(oldFilePath)

        time.sleep(60)

def fetchImageLoop():
    pixiv = PixivFetcher()

    print("Fetch imagel loop started")

    while True:
        pixiv.fetchPixivImages()
        time.sleep(300)
        pixiv.refresh()

def webserver():
    run_server()


   





if __name__ == "__main__":
    fetchThread = threading.Thread(target=fetchImageLoop)
    webserverThread = threading.Thread(target=webserver)
    fetchThread.start()
    webserverThread.start()

    asyncio.run(tagLoop())



