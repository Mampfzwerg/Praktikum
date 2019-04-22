import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

U, N, A = np.genfromtxt('mess1.txt', unpack=True)

t = 125
Ns = N / t
n = np.sqrt(N) / t

#AUSGEWÄHLTE MESSWERTE
U2, N2 = np.genfromtxt('mess2.txt', unpack=True)

Ns2 = N2 / t
n2 = np.sqrt(N2) / t

params, covariance_matrix = np.polyfit(U2, Ns2, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
#print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(U) - 10, np.max(U) + 10)


plt.errorbar(U, Ns, yerr=n, fmt='o',label='Messwerte')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlim(np.min(U) - 10, np.max(U) + 10)
plt.xlabel(r'$U \: / \: V$')
plt.ylabel(r'$\frac{N}{t} \: / \: \frac{1}{s}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')

a = ufloat(0.003, 0.0056)
b = ufloat(88.764, 2.8337)

N3 = np.genfromtxt('mess3.txt', unpack=True)
t3 = 100
Ns3 = N3 / t3
n3 = np.sqrt(N3) / t3

r1 = ufloat(235.14, 1.53)
r2 = ufloat(350.81, 1.87)
r12 = ufloat(566.51, 2.38)

T = (r1 + r2 - r12) / (2 * r1 * r2)

print(T)







