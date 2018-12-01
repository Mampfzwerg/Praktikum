import numpy as np
from uncertainties import ufloat

#ob er behindert ist, das ist richtig

cw = 4.18
my = 155.22
Ty = 349.15
Tm = 317.95
mx = 157.64
Tx = 295.25

#print((cw*my*(Ty-Tm)-cw*mx*(Tm-Tx))/(Tm - Tx))

ck = 1.03
M = 27
a = 23.5*1e-6
k = 75*1e9
p = 2.7
Vo = M/p*1e-6
T = 300.55

#print(Vo)

#print(ck*M-9*a**2*k*Vo*T)

ck2 = ufloat(0.541,0.044)
M2 = 63.5
a2 = 16.8*1e-6
k2 = 136*1e9
p2 = 8.96
Vo2 = M2/p2*1e-6
print(Vo2)
T2 = ufloat(300.62, 0.25)

print(ck2*M2-9*a2**2*k2*Vo2*T2)