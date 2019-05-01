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

z = np.linspace(np.min(x), np.max(x))
l = 633 * 1e-9

def I(x, A, b):
    return A**2 * b**2 * (l / (np.pi * b * (x / K)))**2 * (np.sin(np.pi * b * (x / K) /l))

#par, cov = optimize.curve_fit(I, x, y)
#plt.plot(x, I(*par), 'b-', label=r'Ausgleichskurve', linewidth=1)
#
#A = ufloat(par[0], np.sqrt(cov[0][0]))
#b = ufloat(par[1], np.sqrt(cov[1][1]))



params, covariance_matrix = curve_fit(I, x, y)
#x_plot = np.linspace(10, 10**4, 1000000)
plt.plot(z, I(z, params[0], params[1]), 'b-', label=r'Ausgleichskurve')

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.4f} ± {:.5f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))



#l = ufloat(par[2], np.sqrt(cov[2][2]))

#def h (x, x0, y, a):
#    return a/((x**2-x0**2)**2+y**2*x0**2)
#
#par, cov = optimize.curve_fit(h, U[5:], f[5:])
#x_plot = np.linspace(19.7, 40.3, 1000)
#plt.plot(x_plot, h(x_plot, *par), 'b-', label=r'Ausgleichskurve', linewidth=1)
#
#plt.plot(U, f, 'rx', label='Messdaten')
#plt.xlabel(r'$\nu \: / \: $kHz')
#plt.ylabel(r'$U_A \: / \:$ V')
#
#x0 = ufloat(par[0], np.sqrt(cov[0][0]))
#y = ufloat(par[1], np.sqrt(cov[1][1]))
#a = ufloat(par[2], np.sqrt(cov[2][2]))
#nu_0 = x0


plt.plot(x, y, 'rx', label='Messdaten')
#plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlim(np.min(x) - 1, np.max(x) + 1)
plt.xlabel(r'$Z$')
plt.ylabel(r'$\sqrt{E_k} \: / \: \sqrt{eV}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')