import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
import scipy.constants as const
from scipy import optimize
from scipy.optimize import curve_fit

from uncertainties import ufloat
import uncertainties.unumpy as unp


#Naturkonstanten:
avo = 6.022*10**(23)
mu_B = 9.274*10**(-24)
mu_0 = 4*np.pi*10**(-7)
k_b  = 1.38*10**(-23)
T = 294 #Raumtemperatur in kelvin

konstante = (mu_B**2 * mu_0)/(3*k_b*T)


L = np.array([6,0,5])
S = np.array([1.5,3.5,2.5])
J = np.array([4.5,3.5,7.5,4])

def g_j(l,s,j): #Lande-Faktor
    oben  = 3*j*(j+1)+s*(s+1)-l*(l+1) #Zäher
    unten = 2*j*(j+1) #Nenner
    return oben/unten

g_Faktor = np.zeros(4)

for i in range(0,3):
    g_Faktor[i] = g_j(L[i],S[i],J[i])

print('Lande-Faktoren: ', g_Faktor)

g_Faktor[3] = 0.72

print('Lande Faktor: ', g_Faktor)

m = np.array([9.0,14.08,15.1,7.87]) # in gramm
M = np.array([168,176,180,346]) # molare Masse in gramm pro mol
rho = np.array([7.24,7.40,7.8,6.26]) #Dichte in Gramm pro cubic cm
#Umrechnen in SI
m=m*10**(-3)
M=M*10**(-3)
rho = rho*10**3
#Berechnung N:
N = np.zeros(4)

for i in range(0,4):
    N[i] = (avo*rho[i])/M[i]
print('Zahl N: ', N)

#Berechnung chi
chi= np.zeros(4)

for i in range(0,4):
    chi[i] = g_Faktor[i]**2*N[i]*J[i]*(J[i]+1)*konstante
print('Chi: ', chi)