import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

# N vienmieriigi sadaliiti gadiijuma skaitlji
# N uniformly distributed random numbers
import numpy
from math import cos
from numpy import random
from matplotlib import pyplot as plt

#print(random.__doc__)
#print(random.uniform.__doc__)
N = 5000
x0 = 0
x1 = 4
y0 = -1
y1 = 1
#pseido-gadiijuma skaitlju generatora grauds
#random.seed(1)
x = random.uniform(x0,x1,N)
'''
k = [0, 0, 0, 0, 0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1
print(k)
'''
y = random.uniform(y0,y1,N)
def f(x):
    return cos(x**2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un taas integraalis (laukums starp funkciju un x ass)')
#nav jeegas ziimeet shaadi plt.plot(x,y)
#plt.plot(x,y,'ko')
N1 = 0
for i in range(N):
    if y[i] >= 0 and y[i] <= f(x[i]) :
        plt.plot(x[i],y[i],'go')
        N1 = N1 + 1
    elif y[i] <= 0 and y[i] >= f(x[i]):
        plt.plot(x[i],y[i],'bo')
        N1 = N1 - 1
    else:
        plt.plot(x[i],y[i],'ro')
S_zinaamais = (x1-x0) * (y1-y0)
S_nezinaamais = (1. * S_zinaamais * N1) / N
print(S_nezinaamais)

plt.show()
