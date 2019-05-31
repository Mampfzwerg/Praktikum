import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

a = ufloat(1.256, 0.0046)

e = 1.60218 *1e-19
k = 1.306 * 1e-23

T = e / (unp.log(a) * k)

print(T)