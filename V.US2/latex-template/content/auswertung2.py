import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

L = 15*1e-2
H = 8.035*1e-2
b = 3.995*1e-3
va = 2730

a, b, c, d, e, f,g  = np.genfromtxt('mess3.txt', unpack=True)
print(np.mean(a/2),np.std(a/2),
    np.mean(b/2),np.std(b/2),
    np.mean(c/2), np.std(c/2),
    np.mean(d/2), np.std(d/2),
    np.mean(e/2), np.std(e/2),
    np.mean(f/2), np.std(f/2),
    np.mean(g/2), np.std(g/2))

bs = np.array([np.mean(g/2),np.mean(f/2), np.mean(e/2),np.mean(d/2), np.mean(c/2),
np.mean(b/2), np.mean(a/2)])

t11, t22 = np.genfromtxt('mess1.txt', unpack=True)

d1 = 0.2*1e-2
vw = 1485
tw = d1/vw

t1 = t11*1e-6-tw*2
t2 = t22*1e-6-tw*2

s1 = va*t1
s2 = va*t2
s11 = s1/2
s22 = s2/2
s = s22+s11
DU = H-s
print(DU*1e3)

print((DU*1e3-bs)/(DU*1e3))