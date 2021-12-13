import math

class Complex:
    def __init__(self,r,i=0.0):
        self.r=r
        self.i=i
    def __add__(self,num):
        a_real=self.r+num.r
        a_imag=self.i+num.i
        return Complex(a_real,a_imag)
    def __sub__(self,num):
        s_real=self.r-num.r
        s_imag=self.i-num.i
        return Complex(s_real,s_imag)
    def __mul__(self,num):
        m_real=self.r*num.r-self.i*num.i
        m_imag=self.i*num.r+self.r*num.i
        return Complex(m_real,m_imag)
    def __truediv__(self,num):
        p = (num.r**2+num.i**2)
        d_real=self.r*num.r+self.i*num.i
        d_imag=self.i*num.r-self.r*num.i
        return Complex(d_real/p,d_imag/p)
    def __abs__(self):
        s_abs=(self.r**2+self.i**2)
        return Complex(math.sqrt(s_abs))
    def __str__(self):
        return '(%s, %si)' % (self.r, self.i)

z1=Complex(1,2)
z2=Complex(3,4)
print("Complex numbers: z1=",z1,"and z2=",z2)
print("Operations:\nadd:",z1+z2,"\nsub:",z1-z2,"\nmul:",z1*z2,"\ndiv:",z1/z2,"\nz1 abs:",abs(z1),"\nz2 abs:",abs(z2),"\n")
