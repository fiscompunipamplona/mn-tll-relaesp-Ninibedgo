#nave
import math as mt


x=float(input("ingrese la distanciaen años luz de la tierra al planeta x= "))
v=float(input("ingrese la velocidad de la nave como una fraccion de c= "))

d=x*9.5e15
a=1/(mt.sqrt(1-(v**2)))
c=3e8
T=d/v
N=a*(T-((v*d)/c))

print(T,N)


