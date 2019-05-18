import numpy as np
from scipy.stats import sem
import scipy.constants as const
from scipy import optimize
from uncertainties import ufloat
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, Y = np.genfromtxt('mess1.txt', unpack=True)

y = Y - 0.000515
b = 0.15 * 1e-3
L = 1040
K = np.sqrt(x**2 + L**2)
ph = np.arcsin(x / K) / np.pi
#print (phi)

phi = np.linspace(np.min(ph), np.max(ph), 1000)
l = 633 * 1e-9

#phi2 = np.linspace(np.min(ph), np.max(ph), 48)
#sigma = np.ones(48) * 0.5
#sigma = ph / 20
#sigma[np.abs(phi2-0.004+0.002)<0.002] = 1
#noise = ((np.random.randn(48))**2)**(1/2) * sigma
#y = y + noise



def I(x, A, b):
    return A**2 * b**2 * (l / (np.pi * b * x))**2 * (np.sin(np.pi * b * x /l))**2

params, covariance_matrix = curve_fit(I, x, y, p0=[560, b]) #, sigma=1 / sigma**2, absolute_sigma=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('A = {:.4f} ± {:.5f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))


plt.plot(ph, y, 'rx', label='Messdaten')
plt.plot(phi, I(phi, *params), 'b-', label=r'Ausgleichskurve')
#plt.xlim(np.min(ph) - 1, np.max(ph) + 1)
plt.xlabel(r'$\phi \: / \: rad$')
plt.ylabel(r'$I \: / \: \mu A$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')