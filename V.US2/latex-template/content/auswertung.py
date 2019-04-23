import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

L = 15*1e-2
H = 8.035*1e-2
b = 3.995*1e-3
va = 2730



t11, t22 = np.genfromtxt('mess1.txt', unpack=True)

d = 0.2*1e-2
vw = 1485
tw = d/vw

t1 = t11*1e-6-tw*2
t2 = t22*1e-6-tw*2

s1 = va*t1
s2 = va*t2
s11 = s1/2
s22 = s2/2
print(s11)
print(s22)
s = s22+s11
print(s)
print(H-s)