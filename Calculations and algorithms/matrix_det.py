import math
import random
import numpy

def matrix_det():
    k = int(input("Enter preferred matrix size: "))
    matrix = numpy.random.randint(0,100,size = (k,k))
    m_det = numpy.linalg.det(matrix)
    print("Generated matrix:\n",matrix, "\nThe determinant of this matrix is:", m_det)

matrix_det()