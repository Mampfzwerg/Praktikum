import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt

g, b, B = np.genfromtxt('mess5.txt', unpack=True)
G = 0.03

V = B/G

x = 1+1/V
y = 1+V

