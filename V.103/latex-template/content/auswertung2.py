import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y, z = np.genfromtxt('mess2.txt', unpack=True)

L = 552 
x2 = x*10
#Durchbiegung

#print(z-y)

#print((L*x2**2-(x2**3)/3)*1e-5)

#elastizitätsdingens

m = 0.516
g = 9.81
m1 = ufloat(0.0497,0.0004)
I = (np.pi/64)*1e-8

print((m*g)/(2*m1*I))
