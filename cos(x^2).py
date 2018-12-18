# cos(x**2)
print("Cos(x^2) aprekinasana:")
from math import cos
def cos_arg_kvadrataa(x):
    k = 0
    while k < 501:
        if k == 0:
            a = ((-1)**0*x**0)/(1)
            S = a
            print("a0 = %6.2f S0 = %6.2f"%(a,S))
        k = k + 1
        R = ((-1)**1*x**4)/((2*k)*(2*k-1))
        a = a * R
        S = S + a
        if k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
            continue
        if k == 500:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
            continue
    return "cos(x^2) caur summu: %6.2f"%(S)
x = float(input("Ievadiet argumentu x: "))
g = cos(x*x)
print("cos(%.2f*%.2f) = %6.2f"%(x,x,g))
y = cos_arg_kvadrataa(x)
print(y)
print("                500")
print("               _____")
print("               \            k     4*k")
print("                \       (-1)  *  x")
print("cos(2.27*2.27) = >    _________________")
print("                /")
print('               /____       (2 * k)!')
print('                k=0')
print("                                    4")
print("                            (-1) * x")
print("rekurences reizinatajs: ______________________")
print("")
print("                         (2 * k) * (2 * k - 1)")
