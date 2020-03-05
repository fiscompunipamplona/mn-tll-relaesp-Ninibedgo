import math
a=math.log(100)
print(a)
b=math.log10(100)
print(b)

from numpy.random import rand
print(rand())

r=float(input("ingrese el valor de r="))
a=float(input("ingrese el valor del angulo="))
b=a*math.pi/180

x=r*math.sin(b)
y=r*math.cos(b)
print(x,y)

