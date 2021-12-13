import math
import random
import numpy

def matrix_sum():
    m1 = numpy.random.randint(0,100,size = (128,128))
    m2 = numpy.random.randint(0,100,size = (128,128))
    arr=[]
    for row in range(128):
        for column in range(128):
            arr.append(m1[row][column]+m2[row][column])
    m3 = numpy.reshape(arr, (128,128))
    print("Sum of matrix: M1=\n",m1,"\nand M2=\n",m2,"\nis matrix M3=\n",m3)

matrix_sum()