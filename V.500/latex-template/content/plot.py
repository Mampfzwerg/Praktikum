import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

Uo, Io = np.genfromtxt('orange.txt', unpack=True)
Ugr, Igr = np.genfromtxt('gruen.txt', unpack=True)
Uv, Iv = np.genfromtxt('violett.txt', unpack=True)
Ug, Ig = np.genfromtxt('gelb.txt', unpack=True)
Ub, Ib = np.genfromtxt('blau.txt', unpack=True)

#params1, covariance_matrix1 = np.polyfit(Uo, np.sqrt(Io), deg=1, cov=True)
#errors1 = np.sqrt(np.diag(covariance_matrix1))
params2, covariance_matrix2 = np.polyfit(Ugr, np.sqrt(Igr), deg=1, cov=True)
errors2 = np.sqrt(np.diag(covariance_matrix2))
params3, covariance_matrix3 = np.polyfit(Uv, np.sqrt(Iv), deg=1, cov=True)
errors3 = np.sqrt(np.diag(covariance_matrix3))
params4, covariance_matrix4 = np.polyfit(Ug, np.sqrt(Ig), deg=1, cov=True)
errors4 = np.sqrt(np.diag(covariance_matrix4))
params5, covariance_matrix5 = np.polyfit(Ub, np.sqrt(Ib), deg=1, cov=True)
errors5 = np.sqrt(np.diag(covariance_matrix5))

#print('ao = {:.10f} ± {:.10f}'.format(params1[0], errors1[0]))
#print('bo = {:.4f} ± {:.5f}'.format(params1[1], errors1[1]))
print('agr = {:.10f} ± {:.10f}'.format(params2[0], errors2[0]))
print('bgr = {:.4f} ± {:.5f}'.format(params2[1], errors2[1]))
print('av = {:.10f} ± {:.10f}'.format(params3[0], errors3[0]))
print('bv = {:.4f} ± {:.5f}'.format(params3[1], errors3[1]))
print('ag = {:.10f} ± {:.10f}'.format(params4[0], errors4[0]))
print('bg = {:.4f} ± {:.5f}'.format(params4[1], errors4[1]))
print('ab = {:.10f} ± {:.10f}'.format(params5[0], errors5[0]))
print('bb = {:.4f} ± {:.5f}'.format(params5[1], errors5[1]))

def gerade (x, m, b):
    return m*x+b

#z1 = np.linspace(np.min(Uo)-0.5, np.max(Uo)+2)
z2 = np.linspace(np.min(Ugr)-0.9, np.max(Ugr)+1.5)
z3 = np.linspace(np.min(Uv)-0.5, np.max(Uv)+1.5)
z4 = np.linspace(np.min(Ug)-0.5, np.max(Ug)+1.5)
z5 = np.linspace(np.min(Ub)-0.5, np.max(Ub)+2)

#Grüner Plot
plt.plot(Ugr, np.sqrt(Igr), 'gx', label='Messdaten')
plt.plot(z2, gerade (z2, *params2), 'g-', label='Grün')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I}$')
plt.ylim(0,0.5)
plt.xlim(-1.5,3)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

plt.clf()

#Violett

plt.plot(Uv, np.sqrt(Iv), 'mx', label='Messdaten')
plt.plot(z3, gerade (z3, *params3), 'm-', label='violett')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I}$')
plt.ylim(0,0.5)
plt.xlim(-1.5,2)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.clf()

#Gelb

plt.plot(Ug, np.sqrt(Ig), 'yx', label='Messdaten')
plt.plot(z4, gerade (z4, *params4), 'y-', label='Gelb')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I}$')
plt.ylim(0,0.4)
plt.xlim(-1.5,2)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.clf()

#blau

plt.plot(Ub, np.sqrt(Ib), 'bx', label='Messdaten')
plt.plot(z5, gerade (z5, *params5), 'b-', label='Blau')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I}$')
plt.ylim(0,0.3)
plt.xlim(-1.5,1.5)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.clf()
