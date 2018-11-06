import matplotlib.pyplot as plt
import numpy as np


x,y = np.genfromtxt('mess3.txt', unpack=True)

params, covariance_matrix = np.polyfit(x, np.log(y), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(x), np.max(x))

plt.plot(x, np.log(y), 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$1/T \: / \: 1/K$')
plt.ylabel(r'$ln(\eta) \: / \: ln(kg/m*s)$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')