import math
import random
import numpy

def scalar():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    c = []
    d = 0
    for i in range(len(a)):
        c.append(a[i]*b[i])
        d = d+c[i]
    print("The scalar product of vectors: a=",a, "and b=",b, "is: ", d )

scalar()