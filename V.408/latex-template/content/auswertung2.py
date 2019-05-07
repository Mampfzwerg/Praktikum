import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

e, g1, b1, g2, b2 = np.genfromtxt('mess3.txt', unpack=True)

d1 = g1-b1
d2 = g2-b2

print(d1)
print(d2)

f = (e**2-d2**2)/(4*e)
print(np.mean(f), np.std(f))

a = [0.120, 0.240]
print(np.mean(a),np.std(a))