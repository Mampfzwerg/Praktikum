import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

L = 15*1e-2
H = 8.035*1e-2
b = 3.995*1e-3
va = 2730

a, b, c, d, e, f,g  = np.genfromtxt('mess3.txt', unpack=True)
print(np.mean(a),np.std(a),
    np.mean(b),np.std(b),
    np.mean(c), np.std(c),
    np.mean(d), np.std(d),
    np.mean(e), np.std(e),
    np.mean(f), np.std(f),
    np.mean(g), np.std(g))