import numpy as np
from uncertainties import ufloat

a, b, c, d, e, f = np.genfromtxt('mess1.txt', unpack=True)

#Zeit

t = a*60

#Temperaturen 

T1 = b + 273.15
T2 = c + 273.15

#Drücke

pa = (d + 1)*1e5
pb = (e + 1)*1e5

#Differtialquotienten

A = ufloat(-0.00000623,0.00000018)
B = ufloat(0.028, 0.0003)
C = ufloat(294.113,0.1113)

A2 = ufloat(0.0000039,0.00000017)
B2 = ufloat(-0.020, 0.0003)
C2 = ufloat(295.132,0.1077)

#print("Für T1")
#print(2*t*A+B)
#print("Für T2")
#print(2*t*A2+B2)

#Güteziffern

Cp = 4.181
p = 1000
V = ufloat(3, 0.0012)
Ck = 750

#print (Cp*p*V+Ck)

C = Cp*p*V+Ck
t1 = 120
t2 = 360
t3 = 480
t4 = 600

T11 = ufloat (0.02650, 0.00030)
T12 = ufloat (0.02351, 0.00033)
T13 = ufloat (0.02202, 0.00035)
T14 = ufloat (0.02052, 0.00037)

T21i = ufloat (-0.01906, 0.00030)
T22i = ufloat (-0.01719, 0.00032)
T23i = ufloat (-0.01656, 0.00034)
T24i = ufloat (-0.01532, 0.00036)

P1 = 126
P2 = 123
P3 = 122
P4 = 125

#real
#print(C*T11*(1/P1))
#print(C*T12*(1/P2))
#print(C*T13*(1/P3))
#print(C*T14*(1/P4))

#ideal

T1i = 297.05 
T2i = 303.35
T3i = 306.25
T4i = 308.85

T21 = 293.15
T22 = 288.25
T23 = 286.35
T24 = 284.45

#print(T1i/(T1i-T21))
#print(T2i/(T2i-T22))
#print(T3i/(T3i-T23))
#print(T4i/(T4i-T24))

#Verdampfungswärme

A = ufloat(-2071.13,73.68)
R = 8.3144621
M = 120.913

#print(-A*R)
#print((-A*R)/M)

#Massendurchsatz
L = ufloat(142,5)

#print(C*T21i*(1/L))
#print(C*T22i*(1/L))
#print(C*T23i*(1/L))
#print(C*T24i*(1/L))

#Dichte

rho0 = 5.514

pa1 = 460000 
pa2 = 445000
pa3 = 420000
pa4 = 395000
p0 = 100000

pb1 = 675000 
pb2 = 775000
pb3 = 850000
pb4 = 900000

T0 = 273.15

#print(((rho0*pa1*T0)/(p0*T21)))
#print(((rho0*pa2*T0)/(p0*T22)))
#print(((rho0*pa3*T0)/(p0*T23)))
#print(((rho0*pa4*T0)/(p0*T24)))

#Kompressorleistung

k = 1.14
rho1 = 23.63
rho2 = 23.25
rho3 = 22.09
rho4 = 20.92 

m1 = ufloat(-1.78,0.07)
m2 = ufloat(-1.61,0.06)
m3 = ufloat(-1.55,0.06)
m4 = ufloat(-1.43,0.06)

print(((1/(k-1))*(pb1*(pa1/pb1)**(1/k)-pa1)*(1/rho1)*(m1))*(10**-3))
print(((1/(k-1))*(pb2*(pa2/pb2)**(1/k)-pa2)*(1/rho2)*(m2))*(10**-3))
print(((1/(k-1))*(pb3*(pa3/pb3)**(1/k)-pa3)*(1/rho3)*(m3))*(10**-3))
print(((1/(k-1))*(pb4*(pa4/pb4)**(1/k)-pa4)*(1/rho4)*(m4))*(10**-3))

