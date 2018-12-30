import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

a = ufloat(-919.67,45.48)

print(-1/a)

U0 = 51.6
x, y = np.genfromtxt('mess2.txt', unpack=True)

print(y/U0)

