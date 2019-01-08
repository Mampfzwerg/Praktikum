import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

mu = ufloat(1068.4211, 34.31960)
L = ufloat(10.11*1e-3, 0.03*1e-3)
C = ufloat(2.098*1e-9, 0.006*1e-9)

R = 4*np.pi*L*mu 

T = 1/(2*np.pi*mu)

print(2*(L/C)**(1/2))