# Fails: 171.py
# Autors: Karlis Kreilis
# Apliecibas numurs: 260REB181
# Datums: 04.12.2018
# Sagatave funkcijas saknes meklesanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import cos, fabs
def f(x):
    return cos(x*x)
a = 1.1
b = 1.7

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)
if ( funa * funb > 0.0 ):
    print("Dotajaa intervaalaa saknu nav", a, b)
else:
    print("Dotajaa intervaalaa sakne(s) ir!")
# Precizitate
deltax = 0.0001
k = 0
# Sashaurinaashana
while ( fabs(float(b)-float(a)) > deltax):
    k = k + 1
    x = (float(a)+float(b))/2
    funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print("Funkcijas saknes vertiba: x = %.4f "%x)
print("Dotas funkcijas vertiba saja punkta: cos(x^2) = %f "%f(x))
print("Nepieciesamo iteraciju skaits intervalu dalisanai uz pusem: k = ",k)

