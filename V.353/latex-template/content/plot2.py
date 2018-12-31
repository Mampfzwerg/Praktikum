import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, Uc = np.genfromtxt('mess2.txt', unpack=True)

U0 = 51.6
U = Uc/U0

def h (x,m,b):
    return 1/np.sqrt(1+m**2*x**2)+b

params, covariance_matrix = curve_fit(h, f, U)
x_plot = np.linspace(10, 10**4, 1000000)
plt.plot(x_plot, h(x_plot, params[0], params[1]), 'b-', label=r'Ausgleichskurve', linewidth=1)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

plt.plot(f, U, 'rx', label='Messdaten')
plt.xscale('log')
plt.xlabel(r'$f \: / \: \frac{1}{s}$')
plt.ylabel(r'$\frac{U_C}{U_0}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot2.pdf')