# Fails: 171.py
# Autors: Karlis Kreilis
# Apliecibas numurs: 260REB181
# Datums: 03.12.2018
# Sagatave funkcijas saknes meklesanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import cos, fabs
from time import sleep

def cos_arg_kvadrataa(x):
    k = 0
    while k < 501:
        if k == 0:
            a = ((-1)**0*float(x)**0)/(1)
            S = float(a)
        k = k + 1
        R = ((-1)**1*float(x)**4)/((2*k)*(2*k-1))
        a = a * float(R)
        S = S + a
    return S

a = 1.1
b = 1.7

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = cos_arg_kvadrataa(a)
funb = cos_arg_kvadrataa(b)
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
    funx = cos_arg_kvadrataa(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print("Funkcijas saknes vertiba: x = %.4f "%x)
print("Dotas funkcijas vertiba saja punkta: cos(x^2) = %f "%cos_arg_kvadrataa(x))
print("Nepieciesamo iteraciju skaits intervalu dalisanai uz pusem: k = ",k)

