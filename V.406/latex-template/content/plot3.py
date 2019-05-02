import numpy as np
from scipy.stats import sem
import scipy.constants as const
from scipy import optimize
from uncertainties import ufloat
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, Y = np.genfromtxt('mess3.txt', unpack=True)

y = Y - 0.000515
b = 0.15 * 1e-3
L = 1040
K = np.sqrt(x**2 + L**2)
ph = np.arcsin(x / K) / np.pi
#print (phi)

phi = np.linspace(np.min(ph), np.max(ph), 10000)
l = 633 * 1e-9

def I(x, A, b, s):
    return A**2 * (np.cos(np.pi * s * x /l))**2 * (l / (np.pi * b * x))**2 * (np.sin(np.pi * b * x /l))**2
params, covariance_matrix = curve_fit(I, x, y, p0=[0.1308, b, 1e-4]) #0.1308
errors = np.sqrt(np.diag(covariance_matrix))

print('A = {:.4f} ± {:.5f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))
print('s = {:.4f} ± {:.5f}'.format(params[2], errors[2]))


plt.plot(ph, y, 'rx', label='Messdaten')
plt.plot(phi, I(phi, *params), 'b-', label=r'Ausgleichskurve')
#plt.xlim(np.min(ph) - 1, np.max(ph) + 1)
plt.xlabel(r'$\phi \: / \: rad$')
plt.ylabel(r'$I \: / \: \mu A$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot3.pdf')