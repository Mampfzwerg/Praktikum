import matplotlib.pyplot as plt
import numpy as np


y, x = np.genfromtxt('mess3.txt', unpack=True)

# Fehler des Mittelwertes
def mf(k):
    return (np.std(k, ddof=1) / np.sqrt(len(k)))

def mfe(k,l):
    return (np.std(k * l, ddof=1) / np.sqrt(len(k)))

#Ausgleichsgerade
def linaus(a, b, c):
    # 4 Mittelwerte aus m und k
    m1 = np.mean(a*b)
    m2 = np.mean(a)
    m3 = np.mean(b)
    m4 = np.mean(a**2)

    # 4 Mittelwertsfehler aus m und k
    fm1 = mfe(a, b)
    fm2 = mf(a)
    fm3 = mf(b)
    fm4 = mfe(a, a)
    
    # 4 Ableitungen von m
    dm1 = 1 / (m4 - m2**2)
    dm2 = -m3 / (m4 - m2**2) + 2 * m2 * (m1 - m2 * m3) / (m4 - m2**2)**2
    dm3 = -m2 / (m4 - m2**2)
    dm4 = -(m1 - m2 * m3) / (m4 - m2)**2

    # 4 Ableitungen von k
    dk1 = m4 / (m4 - m2**2)
    dk2 = m3 / (m4 - m2**2) + (m3 * m4 - m1 * m2) / (m4 - m2**2)**2
    dk3 = -m2 / (m4 - m2**2) 
    dk4 = -m1 / (m4 - m2**2) + 2 * m2 * (m3 * m4 - m1 * m2) / (m4 - m2**2)**2

    # Gauß'sche Fehlerfortpflanzung: Fehler von m und k
    fm = np.sqrt( (dm1 * fm1)**2 + (dm2 * fm2)**2 + (dm3 * fm3)**2 + (dm4 * fm4)**2)
    fk = np.sqrt( (dk1 * fm3)**2 + (dk2 * fm4)**2 + (dk3 * fm1)**2 + (dk4 * fm2)**2)

    #Steigung
    m = (m1 - m2 * m3) / (m4 - m2**2)
    #Achsenabschnitt
    k = (m3 * m4 - m1 * m2) / (m4 - m2**2)

    print('m: ', m, ' fm: ', fm, ' k: ', k, ' fk: ', fk)
    return(m * c + k)


z = np.linspace(np.min(x) - 5, np.max(x) + 5)

plt.plot(x, y, 'rx', label='Messdaten')
plt.plot(z, linaus(x, y, z), 'b-', label='Ausgleichsgerade')
plt.xlim(np.min(x) - 2, np.max(x) + 2)
plt.xlabel(r'$I \: / \: mA$')
plt.ylabel(r'$U_k \: / \: V$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('plot3.pdf')