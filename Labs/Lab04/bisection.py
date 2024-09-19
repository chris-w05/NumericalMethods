import matplotlib.pyplot as plt
import math
import numpy as np

def bisection( fun, a, b, tol=1e-6, maxits=10, plot_output=False, return_iters=False):
    if np.sign(fun(a)) == np.sign(fun(b)):
        raise ValueError("No root guaranteed")
    iters = 0
    oldC = None
    while iters < maxits:
        iters += 1
        c = (a + b) / 2
        if iters > 1:
            errorApprox = (c - oldC) / c
            if np.abs(b - a) / 2 < tol or np.abs(errorApprox) <= tol:
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
        
        if np.sign(fun(c)) == np.sign(fun(a)):
            a = c
        else:
            b = c
        oldC = c
    
    if iters == maxits:
        raise RuntimeError(f"Maximum number of iterations exceeded: {iters} iterations")
    
    if plot_output:
        plt.show()
    
    if return_iters:
        return iters
    else:
        return c


def expected_iterations(a, b, error):
    return math.log((b-a)/error)/math.log(2)

#Validation:
func = lambda x: x**2 - 1
x = bisection(func, .5, 1, maxits=20, plot_output=True)
print(f'x root at: {x}')
