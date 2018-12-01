import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y, z = np.genfromtxt('mess3.txt', unpack=True)

L = 603
x2 = x*10
#Durchbiegung

#print(z-y)

#print((2*L**2*x2-4*x2**3)*1e-5)

m = 1.2033
g = 9.81
m1 = ufloat(0.00449,0.00004)
I = (1/12)*1e-8


print((m*g)/(48*m1*I))