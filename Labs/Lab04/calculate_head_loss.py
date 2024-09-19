from colebrook_equation import colebrook_equation
from bisection import *

def calculate_head_loss(L):
    # Problem parameters
    e = 0.0002  # meters
    D = 0.25    # Pipe diameter meters
    rho = 1000  # Fluid density kg/m^3
    mu = 6e-4   # Dynamic viscosity Pa.s
    V = 10      # Fluid velocity m/s
    Re = (rho * V * D) / mu #Reynolds number
    print(f'Reynold\'s number is {Re:.5}')
    g = 9.8     #m/s^2

    #Turns colebrook_equation into a function handle of one variable
    colebrook_one_term = lambda f: colebrook_equation(f, e, D, Re)
    f = bisection(colebrook_one_term, .001, .1, tol=1e-10, maxits=50)
    print(f'Frictional coefficient of {f}')
    
    return f*L*V**2/(D*2*g)

head_loss = calculate_head_loss(110)
print(f'The head loss is {head_loss:.5} meters')


tolerance = .01
expect_iterations = expected_iterations(0, 3, tolerance)
func = lambda x: x**2 - 1
actual_iterations = bisection(func, 0, 3, tol=tolerance, maxits=100, return_iters=True)
print(f'For a tolerance of {tolerance}, expect to use {expect_iterations:.5} iterations.')
print(f'My code used {actual_iterations} iterations to find a root with {tolerance} tolerance')

#Looking at the graph, I expect to have a frictional value of 0.015
#In reality, my code returns a value of 0.0112
