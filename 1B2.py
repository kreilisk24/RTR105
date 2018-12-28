import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import *
x = linspace(0, 4, 70)
#print(x)
y = sin(x)
#print(y)
f1 = x
f = float(1*2*3)
s = (x**3/f)
f2 = f1 - s
f3 = f2 + (x**5)/(f*4*5)
f4 = f3 - (x**7)/(f*4*5*6*7)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $sin(x)$")
plt.plot(x, y, color = "#000000", label="sin")
plt.plot(x, f1, label="f1")
plt.plot(x, f2, label="f2")
plt.plot(x, f3, label="f3")
plt.plot(x, f4, label="f4")
plt.legend()
plt.show()
