import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y, z = np.genfromtxt('mess4.txt', unpack=True)

L = 603
x2 = x*10
#Durchbiegung

#print(z-y)

#print((4*x2**3-12*L*x2**2+9*L**2*x2-L**3)*1e-5)

m = 1.2033
g = 9.81
m1 = ufloat(0.00308,0.00001)
I = (1/12)*1e-8

#print((m*g)/(48*m1*I))

x = np.array([6.57e4, 9.581e4])
print(np.mean(x),np.std(x))
