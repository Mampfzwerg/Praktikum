import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

l, U = np.genfromtxt('mess1.txt', unpack=True)

f = ((2.99*10**8)/(l*10**-9))/(10**14)

params, covariance_matrix = np.polyfit(f, U, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.15f} ± {:.15f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(0, np.max(f))

plt.plot(f, U, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$f \,/\, 10^{14} Hz$')
plt.ylabel(r'$U_g \,/\, V$')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig('plot5.pdf')