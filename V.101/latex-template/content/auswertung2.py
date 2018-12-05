import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

T1 = ufloat(8.45,0.5)
T2 = ufloat(7.99,0.5)
T3 = ufloat(8.05,0.5)
T4 = ufloat(8.05,0.5)
T5 = ufloat(8.12,0.5)

T71 = np.array([T1, T2, T3, T4, T5])
T = T71/7
#print(T)

D = ufloat(23.34e-3,1.43e-3)

IZ = (T**2*D)/(4*np.pi**2)

#print(np.mean(IZ))

T6 = ufloat(12.11,0.5)
T7 = ufloat(11.84,0.5)
T8 = ufloat(12.10,0.5)
T9 = ufloat(11.62,0.5)
T10 = ufloat(11.82,0.5)

T72 = np.array([T6, T7, T8, T9, T10])
T21 = T72/7
#print(T21)

IK = (T21**2*D)/(4*np.pi**2)

#print(np.mean(IK))

#Nochmal zum Eigenträgheitsmoment

m = 2*0.2218

#print((4*np.pi**2*m)/D)

#Theoretische Trägheitsmomente

mz = 1.0059
dz = ufloat (0.0795, 0.0005)
rz = dz/2
#print(rz)
print((1/2)*mz*rz**2)

mk = 0.8124
rk = ufloat(0.075,0.0005)

print((2/5)*mk*rk**2)