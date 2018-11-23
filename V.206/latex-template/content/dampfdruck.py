import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

a, b, c, d, e, f = np.genfromtxt('mess1.txt', unpack=True)

pa = (d + 1)
T2 = c + 273.15

#print(np.log(pa))
#print(1/T2)

params, covariance_matrix = np.polyfit(1/T2, np.log(pa), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(1/T2), np.max(1/T2))

plt.plot(1/T2, np.log(pa), 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$1/T_2 \: / \: 1/K$')
plt.ylabel(r'$ln(p_a/1 bar)$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot2.pdf')