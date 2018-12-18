import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

# N vienmieriigi sadaliiti gadiijuma skaitlji
# N uniformly distributed random numbers
import numpy
from math import cos
from numpy import random
#print(random.__doc__)
#print(random.uniform.__doc__)
N = 2500
l = -1
c = 4
#pseido-gadiijuma skaitlju generatora grauds
#random.seed(1)
x = random.uniform(l,c,N)
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
y = random.uniform(l,c,N)
    
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un taas integraalis (laukums starp funkciju un x ass)')
#nav jeegas ziimeet shaadi plt.plot(x,y)
#plt.plot(x,y,'ko')
N1 = 0
for i in range(N):
    if y[i] > 0 and y[i] < cos(x[i]**2) :
        plt.plot(x[i],y[i],'go')
        N1 = N1 + 1
    elif y[i] < 0 and y[i] > cos(x[i]**2):
        plt.plot(x[i],y[i],'go')
        N1 = N1 - 1
    else:
        plt.plot(x[i],y[i],'ro')
S_zinaamais = (c-l) * (c-l)
S_nezinaamais = 1. * S_zinaamais * N1 / N
print(S_nezinaamais)

plt.show()
