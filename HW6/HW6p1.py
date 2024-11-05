import numpy as np
import matplotlib.pyplot as plt
import Linsolve 

def F(x):
    return -x

plt.figure()
for i in [5, 2.5, 1.25, .625, .0375]:
    params = [7/i**2 + 1/i ,    #alpha
              -14/i**2 - 1,     #beta
              7/i**2 - 1/i]     #gamma
    results, independent = Linsolve.BVPsolve(0, 20, 5, 8, i, params, F, solveMethod='Gauss')
    plt.plot(independent, results, label=f'h = {i}')
plt.title('BVP solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

