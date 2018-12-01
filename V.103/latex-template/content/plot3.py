import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y, z = np.genfromtxt('mess3.txt', unpack=True)

L = 603
x2 = x*10
#Durchbiegung

D = z-y

L1=(2*L**2*x2-4*x2**3)*1e-5

params, covariance_matrix = np.polyfit(L1, D, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(L1), np.max(L1))

plt.plot(L1, D, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$3Lx²-4x³  \: / \: 10^5\cdot mm³$')
plt.ylabel(r'$D \: / \: mm$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot3.pdf')