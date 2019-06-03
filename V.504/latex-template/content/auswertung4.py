import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

a = ufloat(-4.932, 0.0758)

e = 1.60218 *1e-19
k = 1.306 * 1e-23

T = -e / (a * k)

#print(T)

i, u, i2 = np.genfromtxt('mess7.txt', unpack=True)

sigma = 5.7 * 1e-12
f = 0.35
nu = 0.28
h = 6.626 * 1e-34
m = 9.109 * 1e-31
q = 1.602 * 1e-19

T = ((u*i - 1)/(f*sigma*nu))**(1/4)

e0 = - k * T * np.log(i2 * h**3 / (f * 4 * np.pi * m * q * k**2 * T**2))
e0 = e0 * 6.242 * 1e18

m = np.mean(e0)
n = np.std(e0, ddof=1) / np.sqrt(len(e0))
o = ufloat(m, n)

print(o)