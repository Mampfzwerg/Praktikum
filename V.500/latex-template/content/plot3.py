import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

U, I = np.genfromtxt('mess2.txt', unpack=True)

plt.plot(U, I, 'rx', label='Messdaten')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$I \,/\, nA$')
plt.legend(loc='best')
plt.ylim(0,0.5)
plt.xlim(0,3)

plt.tight_layout()
plt.savefig('plot6.pdf')