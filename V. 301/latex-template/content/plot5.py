import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


x, y = np.genfromtxt('mess5.txt', unpack=True)

#Messwerte
plt.plot(x, y, 'rx', label='Gemessene Leistung')

#Theoriekurve
def theorie(ra):
    u0 = 1.68
    ri = 5.66
    return (u0**2 * ra) / (ra + ri)**2

z = np.linspace(0, np.max(x))
plt.plot(z, theorie(z), 'b-', label='Theoriekurve')

plt.xlabel(r'$R \: / \: \Omega$')
plt.ylabel(r'$P \: / \: W$')

plt.legend(loc='best')

plt.savefig('plot5.pdf')