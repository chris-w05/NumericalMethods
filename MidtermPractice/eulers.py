def f(x):
    return -1/x

guess = 1
for i in range(0,2)  :
    guess = guess + f(guess)*.1
    
print(guess)

def f2(x,y):
    return x-y

import numpy as np
import matplotlib.pyplot as plt

# Define the ODE function
def f(x, y):
    return x-y  # Example function

# Heun's Method
def heuns_method(f, x0, y0, x_end, h):
    n = int((x_end - x0) / h)  # Number of steps
    x = np.linspace(x0, x_end, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    
    for i in range(n):
        k1 = f(x[i], y[i])  # Slope at the beginning of the interval
        y_predict = y[i] + h * k1  # Euler prediction
        k2 = f(x[i + 1], y_predict)  # Slope at the end of the interval
        y[i + 1] = y[i] + h * 0.5 * (k1 + k2)  # Heun's correction (trapezoidal)
    
    return x, y

# Parameters
x0 = 0  # Initial x value
y0 = 0  # Initial y value (y(x0))
x_end = 2  # End of x range
h = 0.4  # Step size

# Solve using Heun's Method
x_values, y_values = heuns_method(f, x0, y0, x_end, h)

print(x_values)
print(y_values)
# Plot the solution
plt.plot(x_values, y_values, label="Heun's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Heun's Method for Solving ODE")
plt.legend()
plt.grid(True)
plt.show()
