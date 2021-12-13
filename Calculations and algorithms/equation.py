import math
import random
import numpy

def quadratic_equation():
    print("Function: y = ax^2+bx+c")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    delta = pow(b, 2)-4*a*c
 
    if delta>0:
        delta_sqrt = math.sqrt(delta)
        x1 = (-b-delta_sqrt)/(2*a)
        x2 = (-b+delta_sqrt)/(2*a)
        print("There are two roots: x1 =",x1," and x2 =",x2)
    elif delta==0:
        x = -b/(2*a)
        print("There is only one root: x =",x)
    else:
        print("There is no roots!")

quadratic_equation()