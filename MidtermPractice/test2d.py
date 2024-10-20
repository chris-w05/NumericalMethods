import numpy as np
import matplotlib.pyplot as plt

# Sample data for x and y in 2D
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
z = np.array([2, 4, 12, 30, 68, 132, 226, 364, 562, 838])  # Corresponding z-values for each (x, y)

# Create a grid of x and y
X, Y = np.meshgrid(x, y)

# Since z depends on both x and y, we need to generate a 2D grid for z values.
# Here we assume z is some function of X and Y; for simplicity, we'll keep z as a function of x alone.
Z = np.array([2, 4, 12, 30, 68, 132, 226, 364, 562, 838])

# Perform polynomial fitting in two dimensions using least squares
degree = 2

# Create design matrix for 2D polynomial fit (terms: 1, x, y, x^2, y^2, xy, etc.)
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = Z.flatten()

A = np.vstack([X_flat**i * Y_flat**j for i in range(degree+1) for j in range(degree+1-i)]).T

# Solve for polynomial coefficients using least squares
coefficients, _, _, _ = np.linalg.lstsq(A, Z_flat, rcond=None)

# Generate a grid for plotting
x_line = np.linspace(min(x), max(x), 100)
y_line = np.linspace(min(y), max(y), 100)
X_line, Y_line = np.meshgrid(x_line, y_line)

# Generate polynomial surface using the coefficients
Z_line = sum(coefficients[k] * (X_line ** (i - j)) * (Y_line ** j) 
             for k, (i, j) in enumerate([(i, j) for i in range(degree+1) for j in range(degree+1-i)]))

# Plotting the data points and polynomial surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter the original data points
ax.scatter(X, Y, Z, label='Data points')

# Plot the polynomial surface
ax.plot_surface(X_line, Y_line, Z_line, color='red', alpha=0.5)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.legend()
plt.show()

# Display the polynomial coefficients
print("Polynomial coefficients:", coefficients)
