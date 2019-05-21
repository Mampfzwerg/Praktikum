import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

g, b, B = np.genfromtxt('mess1.txt', unpack=True)

A = [g[0],0]
C = [g[1],0]
D = [g[2],0]
E = [g[3],0]
F = [g[4],0]
G = [g[5],0]
H = [g[6],0]
I = [g[7],0]
J = [g[8],0]
K = [g[9],0]
A2 = [0,b[0]]
C2 = [0,b[1]]
D2 = [0,b[2]]
E2 = [0,b[3]]
F2 = [0,b[4]]
G2 = [0,b[5]]
H2 = [0,b[6]]
I2 = [0,b[7]]
J2 = [0,b[8]]
K2 = [0,b[9]]
plt.plot(A, A2 , 'b-')
plt.plot(C, C2 , 'r-')
plt.plot(D, D2 , 'g-')
plt.plot(E, E2 , 'y-')
plt.plot(F, F2 , 'k-')
plt.plot(G, G2 , 'c-')
plt.plot(H, H2 , 'm-')
plt.plot(I, I2 , color = 'darkviolet')
plt.plot(J, J2 , color = 'lime')
plt.plot(K, K2 , color = 'aqua')
plt.plot([0,0.16], [0.16,0.16] , 'k-')
plt.plot([0.16,0.16], [0,0.16] , 'k-')
plt.xlabel(r'$g \: / \: m$')
plt.ylabel(r'$b \: / \: m$')
plt.xlim(0,0.7)
plt.ylim(0,0.5)
plt.tight_layout()
plt.grid(True)
plt.savefig('plot1.pdf')
