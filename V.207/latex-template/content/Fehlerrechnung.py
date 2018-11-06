from uncertainties import ufloat

t = ufloat(80, 0.12)
pf = 998.8
pk = 2.49e3
K = 0.0764e-6

print(K*(pk-pf)*t)

e = ufloat(0.009114, 0.000014)

print(e/((pk-pf)*t))