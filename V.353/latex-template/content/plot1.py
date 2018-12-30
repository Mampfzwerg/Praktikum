import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y = np.genfromtxt('mess1.txt', unpack=True)

x1 = x*1e-3
y1 = np.log(y)

params, covariance_matrix = np.polyfit(x1, y1, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(x1), np.max(x1))

plt.plot(x1, y1, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$t \: / \: \mathrm{s}$')
plt.ylabel(r'$\ln{\left(\frac{U_C}{U_0}\right)}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')