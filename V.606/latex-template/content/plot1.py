import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

U, f = np.genfromtxt('mess1.txt', unpack=True)

plt.plot(U, f, 'rx', label='Messdaten')
plt.xlabel(r'$\nu \: / \: $kHz')
plt.ylabel(r'$U_A \: / \:$ V')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')