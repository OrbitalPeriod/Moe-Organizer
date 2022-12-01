#from saucenao_api import SauceNao
from pysaucenao import SauceNao, GenericSource, BooruSource, PixivSource
from os import listdir, path
import time
from pygelbooru import Gelbooru
from PIL import Image

import utils


class saucehandler:
    def __init__(self):
        self.API = SauceNao(api_key=utils.keys.getSaucenaokey(), db=25, db_mask= 0x1000000,min_similarity=80)
        self.short_term_storage = utils.folders.getShortTermStorage()
        self.gelAPI = Gelbooru(utils.keys.getGelboorukey(), utils.keys.getGelbooruUser())
    
    async def processFile(self, file):     # processes single file in the short term directory, returns (file, [tags,])
        data = [] # [[filename, [tag,]], ]

        editedfile = file
        if path.getsize(self.short_term_storage + "//" + file) > 20000000:
            image = Image.open(self.short_term_storage + "//" + file)
            image.thumbnail((1000,1000))
            image.save(self.short_term_storage + "//" + "xxxxxxx.png")
            editedfile = "xxxxxxx.png"
    
        result = await self.API.from_file(self.short_term_storage + "//" + editedfile)
        
        isOnPixiv = False
        isOnBooru = False
        gelbooruLink = ""

        for i in range(0, len(result)):
            if result.results[i].type == "booru" or result.results[i].type == "generic":
                isOnBooru = True

                if len(result.results[i].urls) == 0:
                    continue

                for y in range (0, len(result.results[i].urls)):
                    if "gelbooru" in result.results[i].urls[y]:
                        gelbooruLink = result.results[i].urls[y]
                        break
                
                break

            elif result[i].type == "pixiv":
                isOnPixiv = True
                continue
        
        if result.long_remaining < 1:
            print("long limit reached, saucehandler going into sleep")
            time.sleep(86400)
        elif result.short_remaining < 1:
            print("Short limit reached, saucehandler going into short sleep")
            time.sleep(30)

        if (isOnPixiv and not isOnBooru):
            print("Image on pixiv but not on booru")
            return (file, ["only on pixiv"])
        elif (isOnBooru and gelbooruLink == ""):
            print("Image on booru, but not on gelbooru")
            return (file, ["Not on gelbooru"])
        elif (not (isOnPixiv or isOnBooru)):
            print("not on pixiv or booru")
            return (file, ["Not found"])
        elif (gelbooruLink != ""): # 'https://gelbooru.com/index.php?page=post&s=view&id=5421359'
            id = gelbooruLink.split("=")[-1]
            try:
                post = await self.gelAPI.get_post(post_id=id)
                tags = post.tags
                return (file, tags)
            except:
                return (file, ["file probably deleted"])


    
    