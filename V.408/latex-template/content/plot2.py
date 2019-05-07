import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

g, b, B = np.genfromtxt('mess5.txt', unpack=True)
G = 0.03

V = B/G
x = 1+1/V
y = 1+V

params, covariance_matrix = np.polyfit(x, g, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(x), np.max(x))

plt.plot(x, g, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$1+1/V$')
plt.ylabel(r'$g \,/\, m$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot2.pdf')