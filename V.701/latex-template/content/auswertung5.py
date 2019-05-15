import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
import scipy.stats as stats

n, N = np.genfromtxt('mess3.txt', unpack=True)

mu = np.mean(N)
sigma = np.std(N)

print(mu, sigma)

plt.hist(N, bins=20)
plt.ylabel('Häufigkeit')
plt.xlabel('N')

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma)*3700, 'b-', label='Gauß-Glocke')
plt.legend(loc='best')
plt.xlim(4200, 5000)
plt.savefig('gauss.pdf')