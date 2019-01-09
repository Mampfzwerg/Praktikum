import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, Uc, U, t = np.genfromtxt('mess2.txt', unpack=True)

UcU = Uc / U

#t1 = t*1e-6

#def h (x,m,b):
#    return m*np.exp(-2*np.pi*b*x)
#
#params, covariance_matrix = curve_fit(h, t1, U)
#x_plot = np.linspace(0,0.0005, 1000000)
#plt.plot(x_plot, h(x_plot, params[0], params[1]), 'b-', label=r'Ausgleichskurve', linewidth=1)
#
#errors = np.sqrt(np.diag(covariance_matrix))
#
#print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
#print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

plt.plot(f, Uc, 'rx', label='Messdaten')
plt.xlabel(r'$f \: / \: kHz$')
plt.ylabel(r'$\frac{U_C}{U}$')
plt.legend(loc='best')

#plt.tight_layout()
plt.savefig('plot2.pdf')