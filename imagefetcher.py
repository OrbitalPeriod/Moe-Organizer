import utils
from pixivapi import Client
from pixivapi import Size
from os import listdir, path
from shutil import move, rmtree
from database import checkPixivID, addpixivID
import time
from pathlib import Path

class PixivFetcher():
    def __init__(self):
        self.short_term_storage = utils.folders.getShortTermStorage()
        self.import_storage = utils.folders.getImportFolder()

        self.client = Client()
        self.client.authenticate(utils.keys.getPixivkey())
        self.refresh_token = self.client.refresh_token
        self.pixivuid = utils.keys.getPixivUID()

        pass
    def refresh(self):
        self.client.authenticate(self.refresh_token)

    def downloadImage(self, pixivID):
        illustration = self.client.fetch_illustration(pixivID)
        illustration.download(directory=Path(self.import_storage), size=Size.ORIGINAL)
    
    def moveImages(self):
        files = listdir(self.import_storage)

        for file in files:
            if path.isdir(self.import_storage + "//" + file):
                files_ = listdir(self.import_storage + "//" + file)
                for file_ in files_:
                    move(self.import_storage + "//" + file + "//" + file_, self.short_term_storage + "//" + file_)
                rmtree(self.import_storage + "//" + file)
            else:
                move(self.import_storage + "//" + file, self.short_term_storage + "//" + file)
    
    def fetchPixivImages(self):
        bookmarks_dict = self.client.fetch_user_bookmarks(self.pixivuid)
        bookmarks = bookmarks_dict["illustrations"]
        for bookmark in bookmarks:
            if not checkPixivID(bookmark.id):
                self.downloadImage(bookmark.id)
                time.sleep(2)
                addpixivID(bookmark.id)
            else:
                continue
        self.moveImages()


