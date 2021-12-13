import os, os.path
from PIL import Image

def files_count():
    dir_path="."
    list = os.listdir(dir_path)
    count_files = len(list)
    print(count_files)

files_count()