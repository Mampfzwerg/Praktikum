import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

a = ufloat(-4.932, 0.0758)

e = 1.60218 *1e-19
k = 1.306 * 1e-23

T = -e / (a * k)

print(T)