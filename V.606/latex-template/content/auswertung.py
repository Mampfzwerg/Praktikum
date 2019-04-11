import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

#Querschnitte

m, l, p = np.genfromtxt('mess2.txt', unpack=True)

print(m/(l*p))
Q = m/(l*p)

#Suszeptibilitäten

U0, R0, Um, Rm = np.genfromtxt('mess3.txt', unpack=True)

F = 86.6*10**-6
#
dR = Rm-R0
R3 = 998
dU = U0-Um
#
x = 2*(dR/R3)*(F/(Q[3]*0.0001))

print(x)
#print(2*((dR*F)/(R0*Q[2])))

#gemittelte Werte

a = np.array([0.0020,0.0024,0.0025])
b = np.array([0.0045,0.0025,0.0016])
c = np.array([0.0032,0.0053,0.0022])
d = np.array([0.0031,0.0044,0.0049])

print(np.mean(a))
print(np.mean(b))
print(np.mean(c))
print(np.mean(d))

