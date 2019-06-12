import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
import sympy
from scipy import optimize

d, t, N1, dN = np.genfromtxt('mess1.txt', unpack=True)