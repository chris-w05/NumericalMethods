from colebrook_equation import colebrook_equation
from bisection import *

# Problem parameters
e = 0.0002  # meters
D = 0.25    # Pipe diameter meters
rho = 1000  # Fluid density kg/m^3
mu = 6e-4   # Dynamic viscosity Pa.s
V = 10      # Fluid velocity m/s
Re = (rho * V * D) / mu #Reynolds number
#Determining type of flow
print(f'Reynold\'s number is {Re:.5}')
if Re > 2300:
    print("Flow is turbulent")
else:
    print("Flow is laminar")
g = 9.8     #m/s^2
L = 110

#bisection params:
a = .001
b = .1
maxiter = 20
plot_output = True


def calculate_head_loss(L):
    #Turns colebrook_equation into a function handle of one variable
    colebrook_one_term = lambda f: colebrook_equation(f, e, D, Re)
    f = bisection(colebrook_one_term, a, b, maxits=maxiter, plot_output=plot_output)
    print(f'Frictional coefficient of {f}')
    return f*L*V**2/(D*2*g)

#Displaying head loss
head_loss = calculate_head_loss(L)
print(f'The resulting head loss is {head_loss:.5} meters')

#Analyzing number of iterations expected vs experimental
tolerance = .01
expect_iterations = expected_iterations(0, 3, tolerance)
func = lambda x: x**2 - 1
actual_iterations = bisection(func, 0, 3, tol=tolerance, maxits=100, return_iters=True)
print(f'For a tolerance of {tolerance}, expect to use {expect_iterations:.5} iterations.')
print(f'My code used {actual_iterations} iterations to find a root with {tolerance} tolerance')

#Looking at the graph, I expect to have a frictional value of about 0.015
#In reality, my code returns a value of 0.0187. This is a slight overestimation of the frictional coefficient
# I would say that this root is reasonable, although there is a 25% error between the values