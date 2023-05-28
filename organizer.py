import os
import shutil

from_dir="C:\Python\C102_assets-main"
to_dir="C:\Python\C102_assets-main"
listofflies=os.listdir(from_dir)
for f in listofflies:
    name,ext=os.path.splitext(f)
    if ext=="":
        continue 
    if ext in[".png",".jpg",".jifif"]:
        path1 = from_dir + '/' + f  
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + f
    if os.pathexists(path2):
        print("moving")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        shutil.move(path1,path2)