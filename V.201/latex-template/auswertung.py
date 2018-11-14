import numpy as np

#hier noch Kalorimeterkapazitätsrechnung einfügen
#der rest funktioniert schon :D

#Massen
#Becher
B1 = 234.3e-3
B2 = 236.97e-3
#Rest
mdeck = 140.64e-3
malum = 254.5e-3 - mdeck
mkupf =377.71e-3 - mdeck

cw = 4.18e3
#cgmg =  

#CtoK
K = 273.15

#Messarrays
mk = np.array([malum, mkupf, mkupf, mkupf])
Tk = np.array([100 + K, 99.7 + K, 100 + K, 100 + K])
Tw = np.array([23.8 + K, 23.5 + K, 23.8 + K, 23.4 + K])
Tm = np.array([27.4 + K, 27.8 + K, 27.4 + K, 27.2 + K])
mw = np.array([744.27e-3 - B1, 751.06e-3 - B2, 751.18e-3 - B2, 751.08e-3 -B2])

def ck(i):
    return ((cw * mw[i] + cgmg) * (Tm[i] - Tw[i])) / (mk[i] * (Tk[i] - Tm[i]))

#gibt in Messreihenfolge aus
for i in range(4):
    print(ck(i))

#hier noch mittelwertrechnung usw.
