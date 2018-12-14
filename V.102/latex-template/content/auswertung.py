import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

#Durchmesser des Drahtes

D = np.array([160, 160, 158])

R = ufloat(np.mean(D/2), np.std(D/2))*1e-4

#Periodendauer ohne Magnetfeld 

a = np.genfromtxt('mess1.txt', unpack=True)

P = ufloat(np.mean(a), np.std(a))

#Trägheitsmoment 

m = ufloat(512.2, 0.20488)
d = ufloat(5.076, 0.00035532)

Tk = (2/5)*m*(d/2)**2

Th = 22.5

T = Tk+Th

#Schubmodul 

L = 68.2
 
G = ((8*np.pi*T*L)/(P**2*R**4))/10
G2 = ufloat(142.2,3.4)

#Querkontraktionszahl 

E = 210

Mu = (E/(2*G2))-1

#Kompressionsmodul 
E2 = 210*1e9

Q = (E2)/(3*(1-2*Mu))

#ZWeiter Teil

#Periodenzeiten

b, c, e, f, g = np.genfromtxt('mess2.txt', unpack=True)

T1 = ufloat(np.mean(b), np.std(b))
T2 = ufloat(np.mean(c), np.std(c))
T3 = ufloat(np.mean(e), np.std(e))
T4 = ufloat(np.mean(f), np.std(f))
T5 = ufloat(np.mean(g), np.std(g))

#Magnetfeldstärke

I = np.array([0.1,0.2,0.3,0.6,0.8])
N = 390
R = 78e-3
Mu0 = 4*np.pi*1e-7

B = (Mu0*8*I*N)/(125**(1/2)*R)

#magnetisches Moment

mf = ufloat(0.16559,0.00294)

print((4*np.pi*T*1e-7)/(mf))

