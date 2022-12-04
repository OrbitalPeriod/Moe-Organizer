git clone the repo  
cd into the folder  
run 'python3 -m venv .'  
run 'Scripts\activate.bat'  
run 'pip install -r requirements.txt'  

enter the required params into config.json (pixiv, pixivUID and saucenao are all mandatory, the pathfiles can all be customized to your liking)  

run 'python3 setup.py'  

run 'python3 main.py' and everything should work  

the long term directory is where images will be stored in the long term  
the short term directory will be used for saving images before they get tagged  
the import directory is the directory from which images will be imported  