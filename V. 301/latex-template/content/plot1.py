import matplotlib.pyplot as plt
import numpy as np

y, x = np.genfromtxt('mess1.txt', unpack=True)

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(x) - 5e-3, np.max(x) + 5e-3)

plt.plot(x, y, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlim(np.min(x) - 5e-3, np.max(x) + 5e-3)
plt.xlabel(r'$I \: / \: mA$')
plt.ylabel(r'$U_k \: / \: V$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')

