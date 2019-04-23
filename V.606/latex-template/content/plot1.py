import numpy as np
from scipy.stats import sem
import scipy.constants as const
from scipy import optimize
from uncertainties import ufloat
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

U,f = np.genfromtxt('mess1.txt', unpack=True)

def h (x, x0, y, a):
    return a/((x**2-x0**2)**2+y**2*x0**2)

par, cov = optimize.curve_fit(h, U[5:], f[5:])
x_plot = np.linspace(19.7, 40.3, 1000)
plt.plot(x_plot, h(x_plot, *par), 'b-', label=r'Ausgleichskurve', linewidth=1)

plt.plot(U, f, 'rx', label='Messdaten')
plt.xlabel(r'$\nu \: / \: $kHz')
plt.ylabel(r'$U_A \: / \:$ V')

x0 = ufloat(par[0], np.sqrt(cov[0][0]))
y = ufloat(par[1], np.sqrt(cov[1][1]))
a = ufloat(par[2], np.sqrt(cov[2][2]))
nu_0 = x0

print('Parameter Gamma: ', y)
print('Parameter a: ', a)
print("Maximalwert: ", nu_0)

nu_p = unp.sqrt(unp.sqrt(unp.sqrt(2)-1)*x0*y + x0**2)
nu_m = unp.sqrt(-unp.sqrt(unp.sqrt(2)-1)*x0*y + x0**2)

print("Neg. Frequnez: ", nu_p)
print("Pos: Frequenz:", nu_m)

# Güte:
Q = nu_0/(nu_p-nu_m)
print("Güte:",Q)

#Gerade 
h = a/(y**2 * x0**2)/np.sqrt(2)
plt.plot(x_plot, 0*x_plot + h.nominal_value, 'g-',label= r'$\frac{U_{A, max}}{\sqrt{2}}$', linewidth=1.3)


plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')