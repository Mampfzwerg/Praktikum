import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

x, y = np.genfromtxt('mess1.txt', unpack=True)

x1 = x*(np.pi/180)


y1 = y*1e-3
r = 30e-2

M = y1*r

params, covariance_matrix = np.polyfit(x1, M, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(x1), np.max(x1))

plt.plot(x1, M, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$\varphi \: / \: rad$')
plt.ylabel(r'$M \: / \: mNm$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')