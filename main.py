import utils
import database
from saucehandler import saucehandler
import asyncio
from os import listdir, remove
import shutil
import time
from PIL import Image
import imagehash
from imagefetcher import PixivFetcher
import threading

async def tagLoop():
    sauce = saucehandler()
    oldFilePath = ""
    PernamentFilePath = ""

    print("Tagloop started")

    while True:
        files = listdir(utils.folders.getShortTermStorage())
        for file in files:
            oldFilePath = utils.folders.getShortTermStorage() + "//" + file
            imageID = database.getmaxID() + 1
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

   





if __name__ == "__main__":
    fetchThread = threading.Thread(target=fetchImageLoop)
    #fetchThread.start()

    asyncio.run(tagLoop())



