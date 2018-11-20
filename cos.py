# cos(x*x)
print("Cos(x^2) aprekinasana:")
from math import cos
def cos_arg_kvadrataa(x):
    for k in [0,499,500]:
        if k == 0:
            a = ((-1)**0*x**0)/(1)
            S = a
            print("a0 = %6.2f S0 = %6.2f"%(a,S))
            continue
        R = (-1)**1*x**4/((2*k)*(2*k-1))
        a = a * R
        S = S + a
        print("a%d = %6.2f S%d = %62f"%(k,a,k,S))
    return
x = float(input("Ievadiet argumentu x: "))
g = cos(x*x)
print("cos(%.2f*%.2f) = %6.2f"%(x,x,g))
y = cos_arg_kvadrataa(x*x)
print(y)

