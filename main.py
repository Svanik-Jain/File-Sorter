import os
import shutil
from tkinter import *
from tkinter import filedialog




AskPath = Tk()
AskPath.withdraw()
mpath = filedialog.askdirectory(title="Select Folder")
AskPath.destroy()
AskPath.mainloop()

os.chdir(mpath)

ListOFFiles = os.listdir(mpath)
ListOFFileExt = []
ListExtI = []
PDFS = []
x=0

print(ListOFFiles)

for i in ListOFFiles:
    ListOFFileExt.append(os.path.splitext(i)[1])

print(ListOFFileExt)
    
for ext in ListOFFileExt:
    if(ext.upper() == ".PDF"):
        if(not os.path.isdir("PDFS")):
            os.makedirs("PDFS")
        shutil.move(f"{ListOFFiles[x]}",f"PDFS/{ListOFFiles[x]}")
    elif(ext.upper() == ".PNG" or ext.upper() == ".JPG"):
        if(not os.path.isdir("IMAGES")):
            os.makedirs("IMAGES")
        shutil.move(f"{ListOFFiles[x]}",f"IMAGES/{ListOFFiles[x]}")
    elif(ext.upper() == ".MP4" or ext.upper() == ".MOV"):
        if(not os.path.isdir("VIDEOS")):
            os.makedirs("VIDEOS")
        shutil.move(f"{ListOFFiles[x]}",f"VIDEOS/{ListOFFiles[x]}")
    elif(ext.upper() == ".TXT" or ext.upper() == ".DOCX"):
        if(not os.path.isdir("DOCS")):
            os.makedirs("DOCS")
        shutil.move(f"{ListOFFiles[x]}",f"DOCS/{ListOFFiles[x]}")
    else:
        if(not os.path.isdir("OTHER")):
            os.makedirs("OTHER")
        shutil.move(f"{ListOFFiles[x]}",f"OTHER/{ListOFFiles[x]}")
    x+=1


