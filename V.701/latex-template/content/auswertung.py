import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

P, N, ch = np.genfromtxt('mess1.txt', unpack=True)

p = P * 1e-3
p0 = 1013 * 1e-3
x0 = 2.4 * 1e-2

x = x0 * p / p0
#print(x * 1e2)

E = 4 / 783 * ch
print(E)
