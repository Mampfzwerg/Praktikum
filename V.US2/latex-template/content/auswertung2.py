import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

L = 15*1e-2
H = 8.035*1e-2
b = 3.995*1e-3
va = 2730

a, b, c, d, e, f,g  = np.genfromtxt('mess3.txt', unpack=True)
print(np.mean(a),
    np.mean(b),
    np.mean(c),
    np.mean(d),
    np.mean(e),
    np.mean(f),
    np.mean(g))