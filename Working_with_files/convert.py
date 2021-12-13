import os, os.path
from PIL import Image

def extentions_converting():
    files = ["first", "second", "third", "fourth"]
    for k in files:
        Image.new('RGB', (1000,1000), color="red").save("images/%s_file.jpg" % k)
        with Image.open("images/%s_file.jpg" % k, "r") as file:
            file.save("images/%s_file.png" % k)

extentions_converting()