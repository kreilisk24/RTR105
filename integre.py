from math import sin, cos, fabs, sqrt
from time import sleep

def f1(x):
    return sqrt(x*x)
k = 5
a = -2
b = 2
I1 = 0.
eps = 0.0001
I2 = (b-a) * ( f1(a) + f1(b) ) / 2
print(I2)
