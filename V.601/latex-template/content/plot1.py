import matplotlib.pyplot as plt
import numpy as np


x,y = np.genfromtxt('mess1.txt', unpack=True)

plt.plot(x, np.log(y), 'rx', label='Messdaten')
plt.ylabel('Steigung')
plt.xlabel(r'$U_A$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot1.pdf')