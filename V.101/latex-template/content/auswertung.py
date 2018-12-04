import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y = np.genfromtxt('mess1.txt', unpack=True)

x1 = x*(np.pi/180)


y1 = y*1e-3
r = 30e-2

#print(y1*r)

#Zweiter Teil

a = np.genfromtxt('mess2.txt', unpack=True)
#print(a**2)

T1 = ufloat(57.93,0.5)
T2 = ufloat(50.30,0.5)
T3 = ufloat(46.89,0.5)
T4 = ufloat(43.00,0.5)
T5 = ufloat(40.10,0.5)
T6 = ufloat(35.72,0.5)
T7 = ufloat(32.58,0.5)
T8 = ufloat(28.85,0.5)
T9 = ufloat(25.49,0.5)
T10 = ufloat(22.36,0.5)

T71 = np.array([T1, T2, T3, T4, T5, T6, T7, T8, T9, T10])
T = T71/7

#print(T**2)

b = ufloat(4.59, 1.99)
D = ufloat(23.34, 1.43)

print((b*D)/(4*np.pi**2))

