import matplotlib.pyplot as plt
import numpy as np

T = np.array([296.15, 427.15, 456.15, 458.15, 461.15])

p = 5.5*10**7*np.exp(-6876/T)
w = 0.0029/p
a = 2

print("Drücke: ",p)
print("Weglänge: ", w)
print("Vergleich: ", a/w)

U = np.array([3.04, 2.53, 2.53, 2.53, 2.79, 2.79, 2.53, 2.39, 3.18, 2.79, 3.29])

print(np.mean(U))

U1 = 5.46
U2 = 8.2
mu = (U1-U2)/(4.135*1e-15)
c = 2.99*1e8
print(c/mu)