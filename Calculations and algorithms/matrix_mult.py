import math
import random
import numpy

def matrix_multiplication():
    matrix1 = numpy.random.randint(0,100,size = (8,8))
    matrix2 = numpy.random.randint(0,100,size = (8,8))
    arr = []
    for row in range(8):
        for column in range(8):
            sum = 0
            for f in range(8):
                sum = sum + matrix1[row][f]*matrix2[f][column]
            arr.append(sum)
    matrix3 = numpy.reshape(arr, (8,8))
    print("First matrix is M1=\n",matrix1,"\nand second matrix is M2=\n",matrix2,"\nthe multiplication is M3=\n",matrix3)    

matrix_multiplication()