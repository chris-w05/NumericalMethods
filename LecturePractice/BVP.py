import numpy as np
import Linsolve
import matplotlib.pyplot as plt


def function ( y2, y1, y):
    return 

def BVP( BV1, BV2, h, ODE ):
    tRange = np.arange(BV1[0], BV2[0], h)
    y = np.zeros_like(tRange)
    y[0] = BV1[1]
    y[-1] = BV2[1]    
    
    return y


def F(x):
    return np.sin(x)*10

h = .05
p = .0001
params = [
    1/h**2,
    p**2 - 2/h**2,
    1/h**2
]


results, independent = Linsolve.BVPsolve(0, 10, 0, 0, h, params, F)
plt.plot(independent, results, label=f'h = {h}')
plt.title('BVP solution')
plt.xlabel('x [ft]')
plt.ylabel('y displacement [ft]')
plt.legend()
plt.show()