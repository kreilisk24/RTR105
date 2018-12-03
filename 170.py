# Fails: 170.py
# Autors: Karlis Kreilis
# Apliecibas numurs: 260REB181
# Datums: 03.12.2018
# Sagatave funkcijas saknes meklesanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

a = 1.1
b = 3.2

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

if ( funa * funb > 0.0 ):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotajaa intervaalaa sakne(s) ir!"

# Precizitate
deltax = 0.01

# Sashaurinaashana
while ( fabs(b-a) > deltax):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print "Saknes ir: ", x
