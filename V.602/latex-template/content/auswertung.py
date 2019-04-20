import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

z, E = np.genfromtxt('mess1.txt', unpack=True)

x = 57.2958
e = 1.602176487 * 1e-16
E = E * e
R = 13.6 * 1.602176487 * 1e-19
sigma = z - np.sqrt(E / R)

h = 6.626 * 1e-34
c = 299792458
d = 201.4 * 1e-12
theta = np.arcsin((h * c) / (E * 2 * d)) * 57.2958



t = ufloat(10, 0.75) / 2
lambdamin = 2 * d  * unp.sin(t / 57.2958)
Emax = h * c / lambdamin
lambdamintheo = h * c /(e  * 35)
Emaxtheo = h * c / lambdamintheo
#print(Emax / e)

a = ufloat(11.89, 0.31)
b = ufloat(14.1, 0.4)
g = b - a
#print((b - a))

# Mehr Energie!!!
t = ufloat(15.0 , 0.4)
E1 = (h * c / (2 * d * unp.sin(t / x)))/ e
#E2 = h * c / (2 * d * np.sin(20.0 / 57.2958)) / e
print(E1)

#Ex = ufloat(9.58, 0.2)
#Ey = ufloat(8.04, 0.14)
##wurzel = ufloat(np.sqrt(9 * e /R), np.sqrt(0.18 * e /R))
#sigma1 = 40 - unp.sqrt(E1 * e / R)
#sigma2 = 29 - 2 * unp.sqrt((R * (29 - sigma1)**2 - Ey * e) / R)
#sigma3 = 29 - 3 * unp.sqrt((R * (29 - sigma1)**2 - Ey * e) / R)
#print(sigma1)






#Auflösung
#print((0.035 + 0.02) / 2) 
#x = np.array([0.035, 0.020])
#print(np.std(x, ddof=1) / np.sqrt(len(x)))



#En = h * c / (2 * d * np.sin(15 / 57.2958))
#print(En / e)
#print(40 - np.sqrt(En / R))

#L-Kante
alpha = 7.2974 * 1e-3
dE = g  * e
sigmaL = 79 - (((4 / alpha) * unp.sqrt(dE / R) - (5 * dE / R)) *
    (1 + (19/32) * alpha**2 * (dE/R)))**(1/2)
print(sigmaL)