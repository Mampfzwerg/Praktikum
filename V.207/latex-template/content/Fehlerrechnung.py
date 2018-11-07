from uncertainties import ufloat

t = ufloat(12.40,0.12)
pf = 998.8
pk = 2.49e3
K = 0.0764e-6

print(K*(pk-pf)*t)

e = ufloat(0.001413, 0.000014)

print(e/((pk-pf)*t))

k = ufloat(493.40e-9, 5e-9)
x = ufloat(71.59,0.41)
y = ufloat(65.80,0.33)
z = ufloat(61.42,0.52)
a = ufloat(53.74,0.16)
b = ufloat(49.64,0.14)
c = ufloat(45.48,0.63)
d = ufloat(43.23,0.07)
e = ufloat(40.30,0.01)
f = ufloat(38.11,0.32)
g = ufloat(36.20,0.11)


print("Viskositäten")
print(k*(pk-pf)*x)
print(k*(pk-pf)*y)
print(k*(pk-pf)*z)
print(k*(pk-pf)*a)
print(k*(pk-pf)*b)
print(k*(pk-pf)*c)
print(k*(pk-pf)*d)
print(k*(pk-pf)*e)
print(k*(pk-pf)*f)
print(k*(pk-pf)*g)

print("Geschwindigkeiten")
print(100/x)
print(100/y)
print(100/z)
print(100/a)
print(100/b)
print(100/c)
print(100/d)
print(100/e)
print(100/f)
print(100/g)
print(100/t)

