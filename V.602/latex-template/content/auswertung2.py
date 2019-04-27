import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

z, E = np.genfromtxt('mess1.txt', unpack=True)


x = 57.2958
e = 1.602176487 * 1e-16
E = E * e
R = 13.6 * 1.602176487 * 1e-19

h = 6.626 * 1e-34
c = 299792458
d = 201.4 * 1e-12

t = ufloat(15.0 , 0.4)
E1 = (h * c / (2 * d * unp.sin(t / x)))/ e

Ex = ufloat(9.58, 0.2)

sigma1 = 29 - unp.sqrt(E1 * e / R)
sigma3 = 29 - 2 * unp.sqrt((R * (29 - sigma1)**2 - Ex * e) / R)
print(sigma3)