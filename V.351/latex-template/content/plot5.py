import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

k, U, Ut = np.genfromtxt('mess5.txt', unpack=True)

print(((Ut - U)**2)**(1/2) / Ut * 100)

T = 1 / 31.25e3

#def fourier(t, k, U, T):
#    e = 0
#    for i in range(9):
#        e += U[i] * np.sin(k[i] * 2 * np.pi * t / T)
#    return e
#
#t = np.linspace(0, 0.0001, 500)
#
#plt.plot(t, fourier(t, k, U, T), 'r-', label='Berechnete Rechteckskurve')
#plt.xlabel(r'$t \:/\: s$')
#plt.ylabel(r'$f(t)$')
#plt.legend(loc='best')
#
##plt.tight_layout()
#plt.savefig('plot5.pdf')