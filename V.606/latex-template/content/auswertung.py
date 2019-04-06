import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

#Querschnitte

m, l, p = np.genfromtxt('mess2.txt', unpack=True)

print(m/(l*p))
Q = m/(l*p)

#Suszeptibilitäten

U0, R0, Um, Rm = np.genfromtxt('mess3.txt', unpack=True)

F = 5

dR = Rm-R0
print(2*((dR*F)/(Rm*Q)))
print(2*((dR*F)/(R0*Q)))

#gemittelte Werte

