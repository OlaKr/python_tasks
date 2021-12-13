import math
from complex import Complex

def calculator():
    z1_re = input("Enter Re for the first complex number: ")
    z1_im = input("Enter Im for the second complex number: ")
    z1_full = Complex(int(z1_re), int(z1_im))
    z2_re = input("Enter Re for the first complex number: ")
    z2_im = input("Enter Im for the second complex number: ")
    z2_full = Complex(int(z2_re), int(z2_im))
    print("Your complex numbers are: z1=",z1_full,"and z2=",z2_full)

    print("Which operation do you want to calculate: +,-,*,/,||?")
    op = input("Enter '+','-','*','/' or '||':")
    if op=="+":
        sum=Complex.__add__(z1_full,z2_full)
        print("Sum of these complex numbers is",sum)
    elif op=="-":
        sub=Complex.__sub__(z1_full,z2_full)
        print("Sub of these complex numbers is", sub)
    elif op=="*":
        mul=Complex.__mul__(z1_full,z2_full)
        print("Mul of these complex numbers is", mul)
    elif op=="/":
        dev=Complex.__truediv__(z1_full,z2_full)
        print("Dev of these complex numbers is", dev)
    elif op=="||":
        ab1=Complex.__abs__(z1_full)
        ab2=Complex.__abs__(z2_full)
        print("The abs for first complex number is",ab1,"and for second complex number is",ab2)
    else:
        print("Wrong operation!")

calculator()