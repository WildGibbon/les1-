from math import *

a = int(input())
b = int(input())
z1 = (cos(radians(a)) - cos(radians(b)))**2 - (sin(radians(a)) - sin(radians(b)))**2
z2 = -4*(sin(radians((a-b)/2))**2)*cos(radians(a+b))
print(round(z1, 3))
print(round(z2, 3))