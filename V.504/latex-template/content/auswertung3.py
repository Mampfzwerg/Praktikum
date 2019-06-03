import matplotlib.pyplot as plt
import numpy as np

u, i = np.genfromtxt('mess6.txt', unpack=True)

U = u + i * 1e-3
print(U)
#I = np.log(i)
#
#params, covariance_matrix = np.polyfit(U, I, deg=1, cov=True)
#
#errors = np.sqrt(np.diag(covariance_matrix))
#
#print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
#print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))
#
#def gerade (x, m, b):
#    return m*x+b
#
#x = np.linspace(np.min(U) - 0.05, np.max(U) + 0.05)
#
#plt.plot(U, I, 'g.', label=r'$I_5$')
#plt.plot(x, gerade (x, *params), 'b-', label='Ausgleichsgerade')
#plt.xlim(np.min(U)-0.05, np.max(U)+0.05)
#plt.ylim()
#plt.xlabel(r'$U \: / \: V$')
#plt.ylabel(r'$\ln{\left(\frac{I}{1nA}\right)}$')
#plt.legend(loc='best')
#plt.grid(True)
#
#plt.tight_layout()
#plt.savefig('plot3.pdf')