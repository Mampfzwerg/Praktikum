import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

z, x1, x2, d, z2 = np.genfromtxt('mess1.txt', unpack=True)

H = 5.046

dH = d / H

lam = dH * 2 / z

#print(dH, lam)

mean = ufloat(np.mean(lam),np.std(lam, ddof=1) / np.sqrt(len(lam)))

mean2 = np.mean(z2)

b = 50 * 1e-3
dn = mean * mean2 / b / 2 *1e-3

T0 = 273.15
T = 298.15
p0 = 1.0132

n = 1 + dn * (T / T0) * (p0 / 0.6)

print(n)