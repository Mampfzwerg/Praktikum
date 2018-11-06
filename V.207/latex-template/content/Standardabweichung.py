import matplotlib.pyplot as plt
import numpy as np

y, x = np.genfromtxt('mess1.txt', unpack=True)

print(np.std(x))
print(np.std(y))