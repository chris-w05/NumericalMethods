import numpy as np
import matplotlib.pyplot as plt
import Linsolve

E = 30000           #ksi
I = 0.03858024688   #in^4
w = 1               #kip/ft
L = 10              #ft

#RHS of ODE
def F(x):
    return w*L*x/2 - w*x**2/2

def analytical(x):
    return w*L*x**3/(12*E*I) - w*x**4/(24*E*I) - w*L**3*x/(24*E*I)

plt.figure()
h = 2
alpha = E*I/h**2
beta = -2*E*I/h**2
gamma = E*I/h**2
params = [alpha, beta, gamma]
results, independent = Linsolve.BVPsolve(0, L, 0, 0, h, params, F,solveMethod='Seidel')

#plotting my results vs analytical
plt.plot(independent, results, label=f'h = {h}')
i = np.arange(0, L, .1)
plt.plot( i, analytical(i), label='Analytical')
plt.title('BVP solution')
plt.xlabel('x [ft]')
plt.ylabel('deflection [ft]')
plt.legend()
plt.show()