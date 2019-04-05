import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

z, E = np.genfromtxt('mess1.txt', unpack=True)

E = E * 1.602176487 * 1e-16
R = 13.6 * 1.602176487 * 1e-19
sigma = z - np.sqrt(E / R)

h = 6.626 * 1e-34
c = 299792458
d = 201.4 * 1e-12
theta = np.arcsin((h * c) / (E * 2 * d)) * 57.2958

print(sigma)

