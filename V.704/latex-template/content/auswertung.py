import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.stats import sem
import scipy.constants as const
from scipy import optimize
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

#import locale
## Set to German locale to get comma decimal separater
#locale.setlocale(locale.LC_NUMERIC, "de_DE")
#plt.rcParams['axes.formatter.use_locale'] = True

def Funktion(x,a,b):
    return a*x + b

d, t, N = np.genfromtxt('mess1.txt', unpack=True)

d = unp.uarray(d,0.1)*10**(-6) #in Meter umrechnen
t = unp.uarray(t,0.0)
#delta N
delta_N =np.zeros(12)
for i in range(0,len(delta_N)):
    delta_N[i] = np.sqrt(N[i])
N = unp.uarray(N,delta_N)
print('Array: ', N)

#Nullrate Array
N_0 = np.ones(12)*551
N_null = unp.uarray(N_0,23.4733)/900
print('Nullraten: ', N_null)

#Aktivität berechnen
a = unp.uarray(np.zeros(12),np.zeros(12))
for i in range(0,len(a)):
    a[i] = abs((N[i]/t[i]-N_null[i]))
print('Aktivitäten: ', a)
#a[10]*=(-1)
#a[9]*=(-1)
#print('Aktivität: ', a)

#d=x-Achse!!
#a=y_Achse!!

plt.errorbar(unp.nominal_values(d),unp.nominal_values(a), xerr = unp.std_devs(d), yerr = unp.std_devs(a) ,fmt = 'x',color='blue',label = r'Messwerte', markersize = 4.5)

params, covariance_matrix = optimize.curve_fit(Funktion, unp.nominal_values(d[7:11]) ,np.log(unp.nominal_values(a[7:11])))
x_plot = np.linspace(0.0000, 0.0003,1000)
plt.plot(x_plot,np.exp(Funktion(x_plot,*params)),'b-',color='darkorange', label=r'Lin. Regression, $f(x)=ax+b$', markersize = 1.2)
print('a=', params[0],'±',np.sqrt(covariance_matrix[0,0]))
print('b=', params[1],'±',np.sqrt(covariance_matrix[1,1]))


d_array = np.array([d[6],d[10]]) #passende Werte für d gemäß den positiven Wesswerten
ln_pos = np.array([a[6],a[10]]) #Werte mit positiven ln


params, covariance_matrix = optimize.curve_fit(Funktion,unp.nominal_values(d[0:6]),np.log(unp.nominal_values(a[0:6])))
x_plot = np.linspace(0.0003,0.0005 ,1000)
plt.plot(x_plot,np.exp(Funktion(x_plot,*params)),'b-',color='forestgreen', label=r'Lin. Regression, $g(x)=cx+d$', markersize = 1.2)
print('c=', params[0],'±',np.sqrt(covariance_matrix[0,0]))
print('d=', params[1],'±',np.sqrt(covariance_matrix[1,1]))


#Schnittpunkt berechnen R_max siehe Berechnungen py

plt.ylabel(r'$\left( \frac{N}{A_0} \right)$')
plt.xlabel(r'$d/m$')

plt.yscale('log')
#plt.xlim(-0.00002, 0.0005)
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('beta.pdf')

#Rmax berechnen

a = ufloat(-28481.6346,8702.7606)
b = ufloat(5.90, 1.19)
c = ufloat(-1079.15,7392.72)
d = ufloat(-2.32,2.8)

R = (d-b)/(a-c)*2710
print(R)

E = 1.92*unp.sqrt((R*0.1)**2+0.22*(R*0.1))
print(E)