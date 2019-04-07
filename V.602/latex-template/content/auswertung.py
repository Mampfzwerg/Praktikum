import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

z, E = np.genfromtxt('mess1.txt', unpack=True)

e = 1.602176487 * 1e-16
E = E * e
R = 13.6 * 1.602176487 * 1e-19
sigma = z - np.sqrt(E / R)

h = 6.626 * 1e-34
c = 299792458
d = 201.4 * 1e-12
theta = np.arcsin((h * c) / (E * 2 * d)) * 57.2958

lambdamin = 2 * d * np.sin(5 / 57.2958)
Emax = h * c / lambdamin
lambdamintheo = h * c /(e  * 35)
Emaxtheo = h * c / lambdamintheo

# Mehr Energie!!!
E1 = h * c / (2 * d * np.sin(22.5 / 57.2958)) / e
E2 = h * c / (2 * d * np.sin(20.0 / 57.2958)) / e
#print(E2 / e)

#sigma2 = 29 - np.sqrt((16 * E2 + 4 * E1) / 15 * R)
#print(sigma2)




#Auflösung
#x = np.array([0.252, 0.353])
#print(np.std(x, ddof=1) / np.sqrt(len(x)))




#En = h * c / (2 * d * np.sin(15 / 57.2958))
#print(En / e)
#print(40 - np.sqrt(En / R))

#L-Kante
alpha = 7.2974 * 1e-3
dE = 1.292  * e
sigmaL = 79 - (((4 / alpha) * np.sqrt(dE / R) - (5 * dE / R)) *
    (1 + (19/32) * alpha**2 * (dE/R)))**(1/2)
print(sigmaL)