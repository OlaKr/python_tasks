import os
import fileinput

def replace():
    dictionary= {"i": "oraz", "oraz": "i", "nigdy": "prawie nigdy", "dlaczego": "czemu"}
    path = "replace_before.txt"
    path2 = "replace_after.txt"
    new_line=[]
    file = open(path, "r")
    for line in file:
        for key, value in dictionary.items():
            if key in line:
                line = line.replace(key,value)
        new_line.append(line)
    file2=open(path2, "w")
    for line in new_line:
        file2.write(line)
    file2.close()

replace()