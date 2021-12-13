import os, os.path
from PIL import Image

def files_print():
    path="."
    list = os.listdir(path)
    for i in list:
        dirs=os.path.join(path, i)
        print(" ",dirs)
        if os.path.isdir(dirs):
            for k in os.listdir(dirs):
                print("     ", k)

files_print()