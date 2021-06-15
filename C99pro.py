import os
import shutil
import time

path = input('Entr the path of the file :')
days = time.time()

for file in os.listdir(path):

    if os.stat(file).st_ctime < days - 30 * 86400:
        
        if os.path.isfile(file):
            os.remove(os.path.join(path, file))
