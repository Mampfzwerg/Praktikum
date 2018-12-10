import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#Kopf

#Halbkugel
r = ufloat(0.032, 0.0005) / 2
Vk1 = (4 / 3) * np.pi * r **3
rk1 = r
#print(rk1, Vk1)

#Kegelstumpf 
r1 = ufloat(0.032, 0.0005) / 2
r2 = ufloat(0.019, 0.0005) / 2
h = ufloat(0.045, 0.0005)
Vk2 = (h * np.pi / 3) * (r1**2 + r1 * r2 + r2**2)
rk21 = r1
rk22 = r2
#print(r1, r2, h, Vk2)

#Halskugel
r = ufloat(0.016, 0.0005) / 2 
Vk3 = (4 / 3) * np.pi * r**3
rk3 = r
#print(r, Vk3)

#Torso

#Quader
a = ufloat(0.0487, 0.0005) 
b = ufloat(0.04, 0.0005)
c = ufloat(0.036, 0.0005)
Vt1 = a * b * c
at1 = a
bt1 = b
ct1 = c
#print(a, b, c, Vt1)

#Zylinder
r = ufloat(0.0257, 0.0005) / 2
h = ufloat(0.0133, 0.0005)
Vt2 = h * np.pi * r**2
rt2 = r
ht2 = h
#print(r, h, Vt2)

#Kegelstumpf
r1 = ufloat(0.0303, 0.0005) / 2
r2 = ufloat(0.0394, 0.0005) / 2
h = ufloat(0.0355, 0.0005) 
Vt3 = (h * np.pi / 3) * (r1**2 + r1 * r2 + r2**2)
rt31 = r1
rt32 = r2
ht3 = h
#print(r1, r2, h, Vt3)

#Arme

#Schulterkugel
r = ufloat(0.016, 0.0005) / 2 
Va1 = (4 / 3) * np.pi * r**3
ra1 = r
#print(r, Va1)

#Bizepszylinder
r = ufloat(0.016, 0.0005) / 2
h = ufloat(0.0428, 0.0005)
Va2 = h * np.pi * r**2
ra2 = r
ha2 = h
#print(r, h, Va2)

#Ellbogenkugel
r = ufloat(0.0116, 0.0005) / 2 
Va3 = (4 / 3) * np.pi * r**3
ra3 = r
#print(r, Va3)

#Unterarmzylinder
r = ufloat(0.0143, 0.0005) / 2
h = ufloat(0.0428, 0.0005)
Va4 = h * np.pi * r**2
ra4 = r
ha4 = h
#print(r, h, Va4)

#Handkugel
r = ufloat(0.0095, 0.0005) / 2 
Va5 = (4 / 3) * np.pi * r**3
ra5 = r
#print(r, Va5)

#Halbzylinder
r = ufloat(0.0155, 0.0005) / 2
h = ufloat(0.0267, 0.0005)
Va6 = np.pi * r**2 * h
ra6 = r
ha6 = h
#print(r, h, Va6)

#Beine

#Oberschenkelkugel
r = ufloat(0.0168, 0.0005) / 2 
Vb1 = (4 / 3) * np.pi * r**3
rb1 = r
#print(r, Vb1)

#Oberschenkelzylinder
r = ufloat(0.0182, 0.0005) / 2
h = ufloat(0.0564, 0.0005)
Vb2 = h * np.pi * r**2
rb2 = r
hb2 = h
#print(r, h, Vb2)

#Kniekugel
r = ufloat(0.0125, 0.0005) / 2 
Vb3 = (4 / 3) * np.pi * r**3
rb3 = r
#print(r, Vb3)

#Unterschenkelzylinder
r = ufloat(0.0147, 0.0005) / 2
h = ufloat(0.0663, 0.0005)
Vb4 = h * np.pi * r**2
rb4 = r
hb4 = h
#print(r, h, Vb4)

#Fußgelenkkugel
r = ufloat(0.0092, 0.0005) / 2 
Vb5 = (4 / 3) * np.pi * r**3
rb5 = r
#print(r, Vb5)

#Fußquader
c = ufloat(0.0108, 0.0005)
a = c / 2
b = ufloat(0.0423, 0.0005)
Vb6 = a * b * c
ab6 = a
bb6 = b
cb6 = c
#print(a, b, c, Vb6)

#Gesamtvolumen
V = Vk1 + Vk2 + Vk3 + Vt1 + Vt2 + Vt3 + 2 * (Va1 + Va2 + Va3 + Va4 + Va5 + Va6) + 2 * (Vb1 + Vb2 + Vb3 + Vb4 + Vb5 + Vb6)
#print(V)

#Masse, Dichte
m = 0.1626
w = m / V
#print(w)

#Massen
mk1 = Vk1 * w
mk2 = Vk2 * w
mk3 = Vk3 * w
mt1 = Vt1 * w
mt2 = Vt2 * w
mt3 = Vt3 * w
ma1 = Va1 * w
ma2 = Va2 * w
ma3 = Va3 * w
ma4 = Va4 * w
ma5 = Va5 * w
ma6 = Va6 * w
mb1 = Vb1 * w
mb2 = Vb2 * w
mb3 = Vb3 * w
mb4 = Vb4 * w
mb5 = Vb5 * w
mb6 = Vb6 * w

#Trägheitsmoment Kopf und Torso
Ik1 = (2 / 5) * mk1 * rk1 ** 2
Ik2 = (3 / 10) * mk2 * ((rk21**5 - rk22**5) / (rk21**3 -rk22**3))
Ik3 = (2 / 5) * mk3 * rk3 ** 2
It1 = (1 / 12) * mt1 * (bt1**2 + ct1**2)
It2 = (1 / 2)* mt2 * rt2**2
It3 = (3 / 10) * mt3 * ((rt32**5 - rt31**5) / (rt32**3 - rt31**3))

#Trägheit Beine (s = Steiner)
Ib1 = (2 / 5) * mb1 * rb1**2
Ib2 = (1 / 2) * mb2 * rb2**2
Ib3 = (2 / 5) * mb3 * rb3**2
Ib4 = (1 / 2) * mb4 * rb4**2
Ib5 = (2 / 5) * mb5 * rb5**2
Ib6 = (1 / 12) * mb6 * (bb6**2 + cb6**2)

#print(Ib1 , Ib2 , Ib3 , Ib4 , Ib5 , Ib6)

#Abstände zur Drehachse
b1 = ufloat(0.0125, 0.0015)
b2 = ufloat(0.016, 0.0015)
b3 = ufloat(0.013, 0.0015)
b4 = ufloat(0.019, 0.0015)
b5 = ufloat(0.014, 0.0015)
b6 = ufloat(0.015, 0.0015)
#
Ib1 = Ib1 + mb1 * b1**2
Ib2 = Ib2 + mb2 * b2**2
Ib3 = Ib3 + mb3 * b3**2
Ib4 = Ib4 + mb4 * b4**2
Ib5 = Ib5 + mb5 * b5**2
Ib6 = Ib6 + mb6 * b6**2
#print(Ib1 , Ib2 , Ib3 , Ib4 , Ib5 , Ib6)

Ik = Ik1 + Ik2 + Ik3 + It1 + It2 + It3 + 2 * (Ib1 + Ib2 + Ib3 + Ib4 + Ib5 + Ib6)

#Trägheit Arme (a = ausgestreckt)
Ia1 = (2 / 5) * ma1 * ra1**2
Ia2 = (1 / 2) * ma2 * ra2**2
Ia2a = ma2 / 4 * (ra2**2 + (ha2**2 / 3))
Ia3 = (2 / 5) * ma3 * ra3**2
Ia4 = (1 / 2) * ma4 * ra4**2
Ia4a = ma4 / 4 * (ra4**2 + (ha4**2 / 3))
Ia5 = (2 / 5) * ma5 * ra5**2
Ia6 = (1 / 2) * ma6 * ra6**2
Ia6a = ma6 / 4 * (ra6**2 + (ha6**2 / 3))

#print(Ib1 , Ib2 , Ib3 , Ib4 , Ib5 , Ib6)

#Abstände zur Drehachse (c = ausgestreckt)
a1 = ufloat(0.030, 0.0015)
a2 = ufloat(0.0275, 0.0015)
a3 = ufloat(0.0275, 0.0015)
a4 = ufloat(0.030, 0.0015)
a5 = ufloat(0.030, 0.0015)
a6 = ufloat(0.030, 0.0015)
#
c1 = ufloat(0.030, 0.0015)
c2 = ufloat(0.059, 0.0015)
c3 = ufloat(0.083, 0.0015)
c4 = ufloat(0.108, 0.0015)
c5 = ufloat(0.131, 0.0015)
c6 = ufloat(0.1465, 0.0015)
#
Ic1 = Ia1  + ma1 * c1**2
Ic2 = Ia2a + ma2 * c2**2
Ic3 = Ia3  + ma3 * c3**2
Ic4 = Ia4a + ma4 * c4**2
Ic5 = Ia5  + ma5 * c5**2
Ic6 = Ia6a + ma6 * c6**2
#
Ia1 = Ia1 + ma1 * a1**2
Ia2 = Ia2 + ma2 * a2**2
Ia3 = Ia3 + ma3 * a3**2
Ia4 = Ia4 + ma4 * a4**2
Ia5 = Ia5 + ma5 * a5**2
Ia6 = Ia6 + ma6 * a6**2

#print(Ic1 , Ic2 , Ic3 , Ic4 , Ic5 , Ic6)

#Endergebnisse
Ia = Ik + 2 * (Ia1 + Ia2 + Ia3 + Ia4 + Ia5 + Ia6)
Ic = Ik + 2 * (Ic1 + Ic2 + Ic3 + Ic4 + Ic5 + Ic6)

#print(Ia, Ic)

#Zeitmessung

t1 = ufloat(3.22, 0.5) / 5
t2 = ufloat(3.16, 0.5) / 5
t3 = ufloat(3.22, 0.5) / 5
t4 = ufloat(3.08, 0.5) / 5
t5 = ufloat(3.17, 0.5) / 5
t6 = ufloat(4.33, 0.5) / 5
t7 = ufloat(4.26, 0.5) / 5
t8 = ufloat(4.20, 0.5) / 5
t9 = ufloat(4.57, 0.5) / 5
t10 = ufloat(4.51, 0.5) / 5

x = np.array([t1, t2, t3, t4, t5])
y = np.array([t6, t7, t8, t9, t10])

#print(x, y)

T1 = np.mean(x)
T2 = np.mean(y)

D = ufloat(23.34, 1.43) * 1e-3

I1 = (T1**2 * D) / (4 * np.pi**2)
I2 = (T2**2 * D) / (4 * np.pi**2)

#print(I1, I2)

#print(I1 / Ia, I2 / Ic)
print((Ia-I1)/Ia*100)
print((Ic-I2)/Ic*100)
