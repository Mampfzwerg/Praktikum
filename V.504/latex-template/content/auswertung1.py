import matplotlib.pyplot as plt
import numpy as np

U1, I1 = np.genfromtxt('mess1.txt', unpack=True)
U2, I2 = np.genfromtxt('mess2.txt', unpack=True)
U3, I3 = np.genfromtxt('mess3.txt', unpack=True)
U4, I4 = np.genfromtxt('mess4.txt', unpack=True)
U5, I5 = np.genfromtxt('mess5.txt', unpack=True)

#Y = Y * 1000
#y = np.sqrt(Y)
#
#
#params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
#
#errors = np.sqrt(np.diag(covariance_matrix))
#
#print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
#print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))
#
#def gerade (x, m, b):
#    return m*x+b

U = np.linspace(np.min(U5) - 5, np.max(U5) + 5)

plt.plot(U1, I1, 'r.', label=r'$I_1$')
plt.plot(U2, I2, 'm.', label=r'$I_2$')
plt.plot(U3, I3, 'b.', label=r'$I_3$')
plt.plot(U4, I4, 'c.', label=r'$I_4$')
plt.plot(U5, I5, 'g.', label=r'$I_5$')

plt.xlim(np.min(U), np.max(U))
plt.xlabel(r'$U \: / \: V$')
plt.ylabel(r'$I \: / \: mA$')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.savefig('plot1.pdf')