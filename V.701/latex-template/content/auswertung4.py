import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

P, N, ch = np.genfromtxt('mess2.txt', unpack=True)

p = P * 1e-3
p0 = 1013 * 1e-3
x0 = 2.9 * 1e-2

x = x0 * p / p0 *1e2
#print(x)

E = 4 / 786 * ch
#print(E)

Pe, Ne, che = np.genfromtxt('mess22.txt', unpack=True)

pe = Pe * 1e-3
xe = x0 * pe / p0 *1e2
Ee = 4 / 786 * che

params, covariance_matrix = np.polyfit(xe, Ee, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(xe)-0.05, np.max(xe)+0.05)

plt.plot(x, E, 'rx', label='Messdaten')
plt.plot(z, gerade(z, *params), 'b-', label='Ausgleichsgerade')
plt.xlim(np.min(x)-0.5, np.max(x)+0.5)
plt.xlabel(r'$x_{eff} \: / \: cm$')
plt.ylabel(r'$E \: / \: MeV$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot4.pdf')