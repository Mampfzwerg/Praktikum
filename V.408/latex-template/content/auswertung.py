import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

g, b, B = np.genfromtxt('mess1.txt', unpack=True)

G = 0.03

v1 = b/g
v2 = B/G

dv = v1-v2

f1=1/b+1/g
f = 1/f1
#print(np.mean(f), np.std(f))

e, g1, b1, g2, b2 = np.genfromtxt('mess2.txt', unpack=True)

d1 = g1-b1
d2 = g2-b2

f3 = (e**2-d1**2)/(4*e)
print(np.mean(f3),np.std(f3))