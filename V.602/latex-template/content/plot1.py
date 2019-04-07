import matplotlib.pyplot as plt
import numpy as np

x, Y = np.genfromtxt('mess2.txt', unpack=True)
Y = Y * 1000
y = np.sqrt(Y)


params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(x) - 3, np.max(x) + 3)

plt.plot(x, y, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlim(np.min(x) - 3, np.max(x) + 3)
plt.xlabel(r'$Z$')
plt.ylabel(r'$\sqrt{E_k} \: / \: \sqrt{eV}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')
