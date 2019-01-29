import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

k, U = np.genfromtxt('mess1.txt', unpack=True)

k1 = np.log(k)
U1 = np.log(U)

print(k1, U1)

def h (x,m,b):
    return m*x + b 

params, covariance_matrix = curve_fit(h, k1, U1)
x_plot = np.linspace(-0.5,2.5, 1000000)
plt.plot(x_plot, h(x_plot, params[0], params[1]), 'b-', label=r'Ausgleichsgerade', linewidth=1)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.7f} ± {:.7f}'.format(params[0], errors[0]))
print('b = {:.7f} ± {:.7f}'.format(params[1], errors[1]))

plt.plot(k1, U1, 'rx', label='Messdaten')
plt.xlabel(r'$ln(k)$')
plt.ylabel(r'$ln \: (U \: / \: V)$')
plt.legend(loc='best')

#plt.tight_layout()
plt.savefig('plot1.pdf')