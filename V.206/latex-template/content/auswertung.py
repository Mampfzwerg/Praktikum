import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

a, b, c, d, e, f = np.genfromtxt('mess1.txt', unpack=True)

#Zeit

t = a*60

#Temperaturen 

T1 = b + 273.15
T2 = c + 273.15

#Drücke

pa = (d + 1)*1e5
pb = (e + 1)*1e5

#Plot

#Erster Plot

params, covariance_matrix = np.polyfit(t, T1, deg=2, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('A = {:.8f} ± {:.8f}'.format(params[0], errors[0]))
print('B = {:.3f} ± {:.4f}'.format(params[1], errors[1]))
print('C = {:.3f} ± {:.4f}'.format(params[2], errors[2]))

def gerade (x, A, B, C):
    return A*x**2+B*x+C

#Zweiter Plot

params2, covariance_matrix2 = np.polyfit(t, T2, deg=2, cov=True)

errors2 = np.sqrt(np.diag(covariance_matrix2))

print('A = {:.8f} ± {:.8f}'.format(params2[0], errors2[0]))
print('B = {:.3f} ± {:.4f}'.format(params2[1], errors2[1]))
print('C = {:.3f} ± {:.4f}'.format(params2[2], errors2[2]))

def gerade (x, A, B, C):
    return A*x**2+B*x+C

z = np.linspace(np.min(t), np.max(t))

plt.plot(t, T1, 'mx', label='Messdaten für T1')
plt.plot(t, T2, 'rx', label='Messdaten für T2')
plt.plot(z, gerade(z, *params), 'b-', label='Ausgleichsgerade für T1')
plt.plot(z, gerade(z, *params2), 'c-', label='Ausgleichsgerade für T2')
plt.xlim(np.min(t) - 5, np.max(t) + 5)
plt.xlabel(r'$t \: / \: s$')
plt.ylabel(r'$T \: / \: K$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')

