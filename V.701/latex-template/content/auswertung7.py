import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
import scipy.stats as stats

#a = ufloat(-103336.130, 5941.4868)
#b = ufloat(229485.2, 11305.162)
#N = 37247
#f = 1 / 3.1
#
#R = (N - b) / a
#print(R)
#
#r = R * 10
#E = (f * r)**(2/3)
#print(E)
#
#c = ufloat(- 0.795, 0.079)
#d = ufloat(3.949, 0.072)
#
#E2 = c * R + d
#print(E2)

a = ufloat(- 72400.86, 5325.81)
b = ufloat(170512.00, 10726.97)
N = 29251.5
f = 1 / 3.1

R = (N - b) / a
print(R)

r = R * 10
E = (f * r)**(2/3)
print(E)

c = ufloat(- 0.863, 0.060)
d = ufloat(3.949, 0.061)

E2 = c * R + d
print(E2)