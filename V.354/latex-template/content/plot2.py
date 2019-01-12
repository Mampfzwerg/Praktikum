import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, Uc, U, t = np.genfromtxt('mess2.txt', unpack=True)

UcU = Uc / U
f1 = f*1e3



plt.axhline(y=2.66, color='b', linestyle='-')
#z = np.linspace(np.min(f), np.max(f))
#plt.plot(z, 1.88, 'b-', label='Ausgleichsgerade')

plt.plot(f, Uc, 'rx', label='Messdaten')
plt.xlabel(r'$f \: / \: kHz$')
plt.ylabel(r'$\frac{U_C}{U}$')
plt.legend(loc='best')

#plt.tight_layout()
plt.savefig('plot2.pdf')