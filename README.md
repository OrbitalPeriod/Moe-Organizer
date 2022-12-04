this is a WIP, its not guaranteed to be stable or work perfectly.

This is a project to tag and find anime imagery locally. it uses gelbooru get the tags and stores them in a sqlite database.  
Saucenao is used to find the gelbooru entry, so a saucenao api key is required.  
Pixiv is used to fetch images. your pixiv bookmarks will automatically be imported and added to the database, a pixiv key is required.
once images are tagged, you can find them by going to 'localhost:8000' in your browser, you can also look for tags.
More features will be added in the future.

git clone the repo  
cd into the folder  
run 'python3 -m venv venv'  
run 'venv\Scripts\activate.bat'  
run 'pip install -r requirements.txt'  

enter the required params into config.json (pixiv, pixivUID and saucenao are all mandatory, the pathfiles can all be customized to your liking)  

run 'python3 setup.py'  

run 'python3 main.py' and everything should work  

the long term directory is where images will be stored in the long term  
the short term directory will be used for saving images before they get tagged  
the import directory is the directory from which images will be imported  