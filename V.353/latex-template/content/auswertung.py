import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

#Zeitkonstante ermitteln - 1. Teil der Auswertung

a = ufloat(-919.67,45.48)

#print(-1/a)

#Verhältnis bestimmen - 2. Teil der Auswertung 

U0 = 51.6
x, y = np.genfromtxt('mess2.txt', unpack=True)

#print(y/U0)

#Perioden aus Frequenzen - 3. Teil der Auswertung 

z, w = np.genfromtxt('mess3.txt', unpack=True)

T = 1/z 
w1 = w*1e-3
phi = (w1/T)*2*np.pi



