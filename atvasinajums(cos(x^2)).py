# print(vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
# print(vars())
from numpy import cos, linspace
# print(vars())

def f(x):
    return cos(x*x)

x = linspace(-4,4,100)
# print(vars())

y = f(x)

from matplotlib import pyplot as plt
legend = []
#print(legend)
#print(plt.__doc__)
plt.axis([-4, 4, -10, 10])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcijas $cos(x^2)$ un taas atvasinaajumi")
plt.plot(x,y,"k")
legend.append("$cos(x^2)$ - default")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$cos(x^2)$ - punkti")
#print(legend)

N = len(x)
deltax = x[1] - x[0]
derivative = []
for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    derivative.append(temp)

plt.plot(x,derivative,"y")
legend.append("$cos(x^2)$ atvasinaajums")
plt.plot(x,derivative,"mo")
legend.append("$cos(x^2)$ atvasinajums - punkti")

#atvas_caur_masivu = []
#for i in range(N-1):
#    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
#    atvas_caur_masivu.append(temp)

#plt.plot(x[0:N-1],atvas_caur_masivu,"m")
#legend.append("$cos(x^2)$ atvasinaajums, izmantojot masiva vertibas")
#plt.plot(x[0:N-1],atvas_caur_masivu,"bo")
#legend.append("$cos(x^2)$ atvasinaajums, izmantojot masivu vertibas - dazhi punkti")
def f2(x):
    return (f(x + deltax) - f(x)) / deltax
atvas2 = []
for i in range(N):
    temp2 = (f2(x[i] + deltax) - f2(x[i])) / deltax 
    atvas2.append(temp2)
plt.plot(x,atvas2,"g")
legend.append("$cos(x^2)$ - 2. kartas atvasinaajums")
plt.plot(x,atvas2,"bo")
legend.append("$cos(x^2)$ - 2.k atvasinajuma punkti")

#print(plt.legend.__doc__)
#plt.legend(legend, loc = "upper left")
plt.legend(legend, loc = 3,fancybox=True, framealpha =0.55, facecolor="white")
plt.show()
