# print(vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
# print(vars())
from numpy import sin, linspace
# print(vars())

def f(x):
    return sin(x)

x = linspace(0,4,11)
# print(vars())

y = f(x)

from matplotlib import pyplot as plt
legend = []
#print(legend)
#print(plt.__doc__)
plt.axis([0, 4, -1, 1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcijas $sin(x)$ un taas atvasinaajumi")
plt.plot(x,y,"k")
legend.append("$sin(x)$ - default - viss ir savienots ar taisnam liinijaam")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$sin(x)$ - tikai dazhi punkti")
#print(legend)

N = len(x)
deltax = x[1] - x[0]
derivative = []
for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    derivative.append(temp)

plt.plot(x,derivative,"y")
legend.append("$sin(x)$ atvasinaajums - viss ir savienots ar taisnam liinijam")
plt.plot(x,derivative,"go")
legend.append("$sin(x)$ atvasinajums - dazhi punkti")

atvas_caur_masivu = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    atvas_caur_masivu.append(temp)

plt.plot(x[0:N-1],atvas_caur_masivu,"m")
legend.append("$sin(x)$ atvasinaajums, izmantojot masiva vertibas - viss ir savienots ar taisnam liinijam")
plt.plot(x[0:N-1],atvas_caur_masivu,"bo")
legend.append("$sin(x)$ atvasinaajums, izmantojot masivu vertibas - dazhi punkti")





plt.plot(0.680,0.620,"ch",markersize = 10)

#print(plt.legend.__doc__)
#plt.legend(legend, loc = "upper left")
plt.legend(legend, loc = 3,fancybox=True, framealpha =0.25, facecolor="red")
plt.show()
