import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
import scipy.stats as stats
from scipy.special import factorial

n, NN = np.genfromtxt('mess3.txt', unpack=True)

m = np.min(NN)
N = np.round(((NN - m) / 100), decimals=0)
print(N)

mu = np.mean(N)
sigma = np.std(N)
#print(mu, sigma)

plt.ylabel(r'$P_\lambda (k)$')
plt.xlabel(r'$k$')


k = [0,1,2,3,4,5,6,7]
P = mu**k / factorial(k, exact=False) * np.exp(-mu)
P2 = [0.02, 0.04, 0.16, 0.24, 0.24, 0.15, 0.12, 0.03]

plt.bar(k, P, color='b', width=-0.4, align='edge', label=r'Theoriewerte')
plt.bar(k, P2, color='c', width=0.4, align='edge', label=r'Messwerte')
plt.legend(loc='best')
plt.savefig('poisson.pdf')