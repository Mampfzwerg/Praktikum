import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

b, c, e, f, g = np.genfromtxt('mess2.txt', unpack=True)

T1 = np.mean(b)
T2 = np.mean(c)
T3 = np.mean(e)
T4 = np.mean(f)
T5 = np.mean(g)

T = np.array([T1, T2, T3, T4, T5])
B = np.array([0.45, 0.90, 1.35, 2.70, 3.60])

params, covariance_matrix = np.polyfit(1/(T**2), B, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(1/(T**2)), np.max(1/(T**2)))

plt.plot(1/(T**2), B, 'rx', label='Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$\frac{1}{T²} \: / \: \frac{1}{s²}$')
plt.ylabel(r'$B \: / \: mT$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')