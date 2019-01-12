import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, Uc, U, t = np.genfromtxt('mess2.txt', unpack=True)

f1 = f*1e3
t1 = t / 1e6
phi = 2 * np.pi - t1 / (1 /f1) * 2 * np.pi

#print(phi)


#plt.axhline(y=1.88, color='b', linestyle='-')
#z = np.linspace(np.min(f), np.max(f))
#plt.plot(z, 1.88, 'b-', label='Ausgleichsgerade')

p1 = np.pi /4
p2 = 3 * np.pi / 4
pres = np.pi /2


plt.plot(f, phi, 'rx', label='Messdaten')
plt.axhline(y=p1, color='b', linestyle='-')
plt.axhline(y=p2, color='b', linestyle='-')
plt.axhline(y=pres, color='g', linestyle='-')


plt.xlabel(r'$f \: / \: kHz$')
plt.ylabel(r'$\Phi \: in \: rad$')
plt.legend(loc='best')

plt.savefig('plot3.pdf')