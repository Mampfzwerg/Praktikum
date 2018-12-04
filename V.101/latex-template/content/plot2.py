import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

a, T = np.genfromtxt('mess3.txt', unpack=True)
a2 = a**2
T2 = T**2


params, covariance_matrix = np.polyfit(a2, T2, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(a2), np.max(a2))

plt.plot(a2, T2, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$a² \: / \: m²$')
plt.ylabel(r'$T² \: / \: s²$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot2.pdf')