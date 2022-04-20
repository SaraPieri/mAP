import pandas as pd
import shutil
import os

folder = '/home/sara.pieri/Documents/SeaDroneSee_challenge/notebooks/yolov-extra-head/exp15/pickles/'
folder_out = './results/'

if os.path.isdir(folder_out): 
    shutil.rmtree(folder_out)
os.mkdir(folder_out)

for filename in os.listdir(folder):
    with open(folder_out+os.path.splitext(filename)[0]+".txt", 'w') as f:
        object = pd.read_pickle(folder+filename)
        
        for i in range(0, len(object)):
            #number.txt <class_name> <left> <top> <right> <bottom>
            f.write(str(object[i].category.id) + " ") 
            f.write(str(object[i].score.value) + " ") 
            f.write(str(object[i].bbox.minx) + " " + str(object[i].bbox.maxy) + " " +str(object[i].bbox.maxx) + " " + str(object[i].bbox.miny) ) 
            f.write("\n")
    f.close()

