# Fails: 170.py
# Autors: Karlis Kreilis
# Apliecibas numurs: 260REB181
# Datums: 03.12.2018
# Sagatave funkcijas saknes meklesanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import cos, fabs
from time import sleep

def f(x):
    return cos(x**2)

a = 1
b = 12

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Precizitate
deltax = 0.0001
k = 0
# Sashaurinaashana
while ( fabs(b-a) > deltax):
    x = (a+b)/2; funx = f(x)
    k = k + 1
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print "Saknes ir: ", x
