import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

mu = ufloat(1068.4211, 34.31960)
L = ufloat(10.11*1e-3, 0.03*1e-3)
C = ufloat(2.098*1e-9, 0.006*1e-9)

R = 4*np.pi*L*mu 

T = 1/(2*np.pi*mu)

#Resonanszüberhöhung

R2 = ufloat(509.5, 0.5)

#print((L**(1/2))/(R2*(C**(1/2))))
#print(np.sqrt(9))

#print(R2/(2*np.pi*L))

s1 = (((1 / (L * C)) - (R2**2 / (2 * L**2)))**2)**(1/4)
s2 = ((R2**2 / (4 * L**2)) + (1 / (L * C)))**(1/2)

#print((1 / (2 * np.pi)) * s1 )
#print(-(R2 / (4 * np.pi * L)) + (1/(2*np.pi)) * s2 )       

#print(1/2**(1/2)*3.76)

print(ufloat(38,1.5)-ufloat(28,1.5))