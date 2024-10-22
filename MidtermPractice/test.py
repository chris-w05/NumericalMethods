import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([-1, -532, 244, 5, 35, 754])

# Fit a polynomial of degree n
n = len(x)-1  # n-th order polynomial
coefficients = np.polyfit(x, y, n)

# Generate a polynomial function from the coefficients
polynomial = np.poly1d(coefficients)

# Plot the results
x_line = np.linspace(min(x), max(x), 100)
y_line = polynomial(x_line)

plt.scatter(x, y, label='Data points')
plt.plot(x_line, y_line, label=f'{n}-th order polynomial', color='red')
plt.legend()
plt.show()

# Display the polynomial coefficients
print("Polynomial coefficients:", coefficients)