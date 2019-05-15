import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

P, N, ch = np.genfromtxt('mess1.txt', unpack=True)

p = P * 1e-3
p0 = 1013 * 1e-3
x0 = 2.4 * 1e-2

x = x0 * p / p0 *1e2
#print(x)

E = 4 / 783 * ch
#print(E)

Pe, Ne, che = np.genfromtxt('mess11.txt', unpack=True)

pe = Pe * 1e-3
xe = x0 * pe / p0 *1e2

params, covariance_matrix = np.polyfit(xe, Ne, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

y = np.linspace(np.min(x)-1, np.max(x)+1)
z = np.linspace(np.min(xe), np.max(xe))

plt.plot(x, N, 'rx', label='Messdaten')
plt.plot(z, gerade(z, *params), 'b-', label='Tangente')
plt.plot(y, gerade(z, 0, 37247), 'm-', label=r'$\frac{N_0}{2}$')
plt.xlim(np.min(x)-0.5, np.max(x)+0.5)
plt.xlabel(r'$x_{eff} \: / \: cm$')
plt.ylabel(r'$N$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')
