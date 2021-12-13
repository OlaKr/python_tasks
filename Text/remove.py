import os
import fileinput

def remove():
    to_remove = ["się", "nigdy", "oraz", " i ", "dlaczego"]
    path = "remove_before.txt"
    path2 = "remove_after.txt"
    new_line=[]
    file = open(path, "r")
    for line in file:
        for rem in to_remove:
            if rem in line:
                line = line.replace(rem,'')
        new_line.append(line)
    file.close()
    file2=open(path2, "w")
    for line in new_line:
        file2.write(line)

remove()

