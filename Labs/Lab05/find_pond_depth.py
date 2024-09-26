import numpy as np
import matplotlib.pyplot as plt
from central_difference import central_difference

def newton(fun, x0, fprime, tol=1e-6, maxiter=10):
    #Check for availability of derivative
    if fprime is None:
        fprime = lambda x: central_difference(fun, x, 1e-4)
    
    #Check if guess is the root
    if (np.abs(fun(x0)) < tol ):
        return x0
    
    #Implement Newton-raphson method
    root = x0
    iter = 0
    while iter < maxiter:
        dx = -fun(root)/fprime(root)    #Increment in x
        root += dx                      #Updated root
        if np.abs(dx) <= tol:           #if tolerance is reached
            break                   
        iter += 1                       #update iteration count
    return root

def solar_pond(depth, density, density_top, zone_height):
    #reformatted from equation 4.1
    fd = density - density_top * np.sqrt(1 + np.tan((np.pi*depth)/(4*zone_height))**2)
    return fd

def solar_pond_deriv(depth, density_top, zone_height):
    #partial derivative of rearranged eq 4.1 in terms of z
    tArg = np.pi*depth/(4 * zone_height)
    numerator = np.pi*density_top*np.tan(-tArg)
    denominator = 4*zone_height*(np.cos(tArg)**2)*np.sqrt(np.tan(tArg)**2 + 1)
    return numerator/denominator


#-------------- ACTUAL SCRIPT -----------------#
#Params:
density = 1200      #kg/m^3
density_top = 1100  #kg/m^3
zone_height = 5     #m
#Function and derivative for solar pond funciton
fun = lambda x: solar_pond(x, density, density_top, zone_height)
fun_deriv = lambda x: solar_pond_deriv(x, density_top, zone_height)
initialGuess = 2

#Graphing estimation of zero
x = np.linspace(0, 5, 1000)
y = np.zeros_like(x)
for i in range(0, len(x)):
    y[i] = fun(x[i])
plt.figure()
plt.plot(x, y)
plt.ylabel('difference in density [kg/m^3]')
plt.xlabel('depth [m]')
plt.grid()
plt.title('Visual representation of zero')
plt.show()

    
#Script
root = newton(fun, initialGuess, fun_deriv)
depth = solar_pond(root, density, density_top, zone_height)
print(f'The depth of the pond is {root:.5}m when the desired density is {density}kg/m^3')

root_numerical = newton(fun, initialGuess, fprime=None)
print(f'The depth of the pond using a numerical approximation is {root_numerical:.5}m for a density of {density}kg/m^3')

difference = root - root_numerical
percent_difference = difference/root
print(f'The difference between the two depth found is: {difference:.5}m which is a {percent_difference:.5}%difference')

'''
I can verify my answer is correct by plugging my value of the depth back into the funciton
to see if it matches the desired depth.

My result of 2.6174m makes sense since a difference of 100kg/m^3 over ~2.5m seems appropriate
for for the increase in water density by depth. 

I saw very minimal differences between my answer using the analytical vs numerical derivative,
specifically a 6.787*10^-16 percent difference, which is negligible at best. This error could 
become much larger if a larger dx is used in the central difference approximation

'''
