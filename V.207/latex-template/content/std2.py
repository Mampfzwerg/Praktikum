import matplotlib.pyplot as plt
import numpy as np

x, y, z, a, b, c, d, e, f, g = np.genfromtxt('mess2.txt', unpack=True)

print(np.mean(x),"+-", np.std(x))
print(np.mean(y),"+-", np.std(y))
print(np.mean(z),"+-", np.std(z))
print(np.mean(a),"+-", np.std(a))
print(np.mean(b),"+-", np.std(b))
print(np.mean(c),"+-", np.std(c))
print(np.mean(d),"+-", np.std(d))
print(np.mean(e),"+-", np.std(e))
print(np.mean(f),"+-", np.std(f))
print(np.mean(g),"+-", np.std(g))
