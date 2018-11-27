import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y, z = np.genfromtxt('mess1.txt', unpack=True)

L = 540
x2 = x*10
#Durchbiegung

#print(z-y)

#print((L*x2**2-(x2**3)/3)*1e-5)

#Elastizitätsmodul

m = 528
g = 9.81e3
m1 = ufloat(1.404e-3,0.249e-3)
I = (1/12)*1e4

print((m*g)/(2*m1*I))