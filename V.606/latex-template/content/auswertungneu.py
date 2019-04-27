import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

F = 86.6*10**-6
R31 = 998

#Querschnitte

Q1 = 0.121*0.0001
Q2 = 0.078*0.0001
Q3 = 0.119*0.0001
Q4 = 0.079*0.0001

Q = np.array([Q1, Q2, Q3, Q4])

#Suszeptibilitäten

U0, R0, Um, Rm = np.genfromtxt('mess3.txt', unpack=True)

dR = Rm-R0
dU = Um-U0

print(dU)

R4 = np.array([0.14,0.2,0.22])
R3 = np.array([0.22,0.36,0.15])
R2 = np.array([0.20,0.11,0.07])
R1 = np.array([0.143,0.17,0.175])

U4 = np.array([48.2,48.1,0.50])
U3 = np.array([0.73,0.90,84.1])
U2 = np.array([0.02,0.0,0.01])
U1 = np.array([0.25,0.06,0.31])


mR4 = ufloat(np.mean(R4), np.std(R4))
mR3 = ufloat(np.mean(R3), np.std(R3))
mR2 = ufloat(np.mean(R2), np.std(R2))
mR1 = ufloat(np.mean(R1), np.std(R1))
mR = np.array([mR1, mR2, mR3, mR4])

mU4 = ufloat(np.mean(U4), np.std(U4))
mU3 = ufloat(np.mean(U3), np.std(U3))
mU2 = ufloat(np.mean(U2), np.std(U2))
mU1 = ufloat(np.mean(U1), np.std(U1))
mU = np.array([mU1, mU2, mU3, mU4])

#Mit R berechnete Suszeptibilitäten

X = (2*mR*F)/(R31*Q)

XU = (4*F*mU*1e-3)/(Q)

XT = np.array([0.026, 0.003, 0.014, 0.001])

print((XT - X)/(XT))
print((XT - XU)/(XT))