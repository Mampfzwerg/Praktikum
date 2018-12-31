import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, y = np.genfromtxt('mess3.txt', unpack=True)

T = 1/f 
y1 = y*1e-3
phi = (y1/T)*2*np.pi

v=f

def f (x, a, m, b):
    return a*np.arctan(m*x)+b

params, covariance_matrix = curve_fit(f, v, phi)
x_plot = np.linspace(10, 10**4, 1000000)
plt.plot(x_plot, f(x_plot, params[0], params[1], params[2]), 'b-', label=r'Ausgleichskurve', linewidth=1)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))
print('c = {:.4f} ± {:.5f}'.format(params[2], errors[2]))

plt.plot(v, phi, 'rx', label='Messdaten')
plt.xscale('log')
plt.xlabel(r'$f \: / \: \frac{1}{s}$')
plt.ylabel(r'$\phi \: / \: rad$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot3.pdf')