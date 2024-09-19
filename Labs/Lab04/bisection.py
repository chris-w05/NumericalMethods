import matplotlib.pyplot as plt
import math
import numpy as np

def bisection( fun, a, b, tol=1e-6, maxits=10, plot_output=False, return_iters=False):
    #Check if there is a root guranteed
    if np.sign(fun(a)) == np.sign(fun(b)):
        raise ValueError("No root guaranteed")
    iters = 0
    oldC = None
    #Looping
    while iters < maxits:
        iters += 1
        #Find midpoint
        c = (a + b) / 2
        if iters > 1:
            #Find error
            errorApprox = (c - oldC) / c
            #If tolerance or error criteria are met, exit loop
            if np.abs(b - a) / 2 < tol or np.abs(errorApprox) <= tol:
                break
        
        #plotting
        if plot_output:
            plt.figure(figsize=(10,6))
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
            plt.grid()
        
        #redefining bounds
        if np.sign(fun(c)) == np.sign(fun(a)):
            a = c
        else:
            b = c
        oldC = c
    
    #Warning that max iterations were acheived
    if iters == maxits:
        raise RuntimeError(f"Maximum number of iterations exceeded: {iters} iterations")
    
    #show all the plots to make an underpaid TA close them all
    if plot_output:
        plt.show()
    
    #Added functionality for checking number of iterations
    if return_iters:
        return iters
    else:
        return c


def expected_iterations(a, b, error):
    return math.log((b-a)/error)/math.log(2)

#Validation:
'''
func = lambda x: x**2 - 1
x = bisection(func, .5, 1, maxits=20, plot_output=True)
print(f'x root at: {x}')
'''


# got bored and trying a recursive bisection function:
def bisection_recursive(fun, a, b, tol=1e-6):
    if np.sign(fun(a)) == np.sign(fun(b)):
        return None
    
    c = (a + b) / 2
    #print(f'recursing, a = {a:.3}, b = {b:.3}, c = {c:.3}, f(c) = {fun(c):.3}')
    
    #End condition
    if np.abs(b - a) < tol or np.abs(fun(c)) < tol:
        return c
    
    #Recursion
    if np.sign(fun(c)) == np.sign(fun(a)):
        return bisection_recursive(fun, c, b)
    else:
        return bisection_recursive(fun, a, c)
    