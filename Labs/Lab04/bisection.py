import matplotlib.pyplot as plt
import math
import numpy as np

def bisection( fun, a, b, tol=1e-6, maxits=10, plot_output=False):
    if np.sign(a) == np.sign(b):
        raise ValueError
    iters = 0
    while iters < maxits:
        iters = iters + 1
        c = (a + b)/2
        if iters > 1:
            errorApprox = (c - oldC)/c
            if np.abs(b-a)/2 < tol or np.abs(errorApprox) <= tol:
                break
        
        if plot_output:
            plt.figure()
            xVals = np.linspace(a, b, 50)
            yVals = list(map(lambda x: fun(x), xVals))
            plt.plot(xVals, yVals )
            plt.plot(a, fun(a), marker='o', linestyle='', label='a')
            plt.plot(b, fun(b), marker='o', linestyle='', label='b')
            plt.plot(c, fun(c), marker='o', linestyle='', label='c')
            plt.legend()
            plt.title(f'Bisection at iteration {iters}')
            plt.ylabel('Function value')
            plt.xlabel('X values')
        
        if np.sign(c) == np.sign(fun(a)):
            a = c
        else:
            b = c
        oldC = c
    
    if iters == maxits:
        raise RuntimeError
    
    if plot_output:
        plt.show()
    
    return c

def func(x):
    return x**3

bisection(func, -2, 2, plot_output=True )

