import math
from fractions import Fraction
# Vl(n) = 1/(n/2)! π^((n-4)) r^n
# Vl(n) = 2^(((k-n)/2))/(k)‼ π^((n-3)) r^n   [ k = 2n–1 ]
# 〖Vl〗_n(R) = 2π/n R^2*Vl(n-2)  


def formulaetest(x):
    pi_p = 0
    c_c = 1
    r = 2
    for i in range(4, x):
        if i%2==0:
            c = (math.factorial(int(i/2)))
            my = f"(1/{c})(π^{i-2})(r^{i})"
            #print(c, r, d)
            
            pi_p += 2
            c_c = (c_c * (2/i))
            c_c0 = Fraction(1/c_c).limit_denominator()
            r += 2
            vnc = f"(1/{c_c0})(π^{pi_p})(r^{i})"
            #print(c_c, vnc)
            print(vnc)
            print(f"{my} = {vnc}", True) if my == vnc else print(f"{my} =/ {vnc}", False)

formulaetest(30)
