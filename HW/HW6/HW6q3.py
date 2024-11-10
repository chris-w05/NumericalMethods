import numpy as np
import matplotlib.pyplot as plt
import Linsolve
import scipy.integrate as sci

#Constants:
h = 20      #W/mK
k = 200     #W/mK
L = 2       #m
D = 0.1     #m
Tinf = 300  #K
Tb = 600    #K
Te = 350    #K

P = D*np.pi
A = np.pi * (D/2)**2
c = h*P/(k*A)           #So I dont have to rewite hP/kA
print(c)

def F(x):
    return -c*Tinf

plt.figure()
h = .04
params = [1/h**2 ,          #alpha
        -2/h**2 - c,        #beta
        1/h**2 ]            #gamma
results, independent = Linsolve.BVPsolve(0, L, Tb, Te, h, params, F)
plt.plot(independent, results, label=f'h = {h}')
plt.title('BVP solution')
plt.xlabel('x [ft]')
plt.ylabel('temperature [K]')
plt.legend()
plt.show()

#The results from my computed results match my results by hand - bless up