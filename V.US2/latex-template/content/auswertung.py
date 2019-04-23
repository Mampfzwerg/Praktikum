import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

L = 15*1e-2
H = 8.035*1e-2
b = 3.995*1e-3
va = 2730

#ASCAN

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
s = s22+s11
DU = H-s

#B-Scan 

tu1, to1, tu2, to2 = np.genfromtxt('mess2.txt', unpack=True)

tu11 = tu1*1e-6-tw*2
to12 = to1*1e-6-tw*2
tu21 = tu2*1e-6-tw*2
to22 = to2*1e-6-tw*2

d2 = to22-tu21
d1 = to12-tu11
a = va*d1
a1 = va*d2


