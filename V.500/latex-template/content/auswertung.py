import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

U,I = np.genfromtxt('orange.txt', unpack=True)

print(np.sqrt(I))

a = ufloat(0.159e-14,0.123e-14)
b = ufloat(0.264,0.750)

print(a/(1.602*10**-19))