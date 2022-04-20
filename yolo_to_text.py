import pandas as pd
import shutil
import os
import imagesize

folder = '/home/sara.pieri/Documents/datasets/SeaDroneSee/val/labels/'
folder_out = '/home/sara.pieri/Documents/mAP/input/ground-truth2/'
folder_images = '/home/sara.pieri/Documents/datasets/SeaDroneSee/val/images/'

if os.path.isdir(folder_out): 
    shutil.rmtree(folder_out)
os.mkdir(folder_out)

for filename in os.listdir(folder):
    img_name = os.path.splitext(filename)[0]
    w_img, h_img = imagesize.get(folder_images+img_name+".png")
    print(img_name, w_img, h_img)

    with open(folder+img_name+".txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.strip().split(' ')
            class_obj = line_list[0]
            cx = float(line_list[1])
            cy = float(line_list[2])
            w = float(line_list[3])
            h = float(line_list[4]) 
            maxx = (cx + w/2) * w_img
            minx = (cx - w/2) * w_img
            maxy = (cy + h/2) * h_img
            miny = (cy - h/2) * h_img 

            with open(folder_out+os.path.splitext(filename)[0]+".txt", 'w') as f_new:
                #number.txt <class_name> <left> <top> <right> <bottom>
                f_new.write(str(class_obj) + " ") 
                f_new.write(str(minx) + " ") 
                f_new.write(str(maxy) + " ") 
                f_new.write(str(maxx) + " ") 
                f_new.write(str(miny) + " ") 
                f_new.write("\n")
                f_new.close()
                
        
    f.close()