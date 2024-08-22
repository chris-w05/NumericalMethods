'''
import numpy as np
import matplotlib.pyplot as plt

# Parameters
Lx, Ly = 1.0, 1.0     # Length of the 2D plane in x and y directions
T = 0.1               # Total time
alpha = 0.01          # Thermal diffusivity
nx, ny = 51, 51       # Number of spatial points in x and y
nt = 1000             # Number of time steps
dx = Lx / (nx - 1)    # Spatial step size in x
dy = Ly / (ny - 1)    # Spatial step size in y
dt = T / nt           # Time step size

# Stability criterion (should be <= 0.5 for stability)
stability_criterion_x = alpha * dt / dx**2
stability_criterion_y = alpha * dt / dy**2
if stability_criterion_x > 0.5 or stability_criterion_y > 0.5:
    raise ValueError("The scheme is unstable! Decrease dt or increase dx/dy.")

# Initialize temperature distribution
u = np.zeros((nx, ny))
u_new = np.zeros((nx, ny))

# Initial condition: a Gaussian pulse in the middle of the plane
for i in range(nx):
    for j in range(ny):
        x = i * dx
        y = j * dy
        u[i, j] = np.exp(-100 * ((x - Lx/2)**2 + (y - Ly/2)**2))

# Set up the plot
plt.figure(figsize=(8, 6))
plt.imshow(u, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot')
plt.colorbar(label='Temperature')
plt.title('Initial Condition')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Time stepping loop
for n in range(nt):
    # Update the temperature distribution using FTCS
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u_new[i, j] = (u[i, j] + stability_criterion_x * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +
                           stability_criterion_y * (u[i, j+1] - 2*u[i, j] + u[i, j-1]))
    
    # Update the old temperature distribution
    u = u_new.copy()
    
    # Plot at certain time steps
    if n % (nt // 5) == 0:
        plt.figure(figsize=(8, 6))
        plt.imshow(u, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot')
        plt.colorbar(label='Temperature')
        plt.title(f'Temperature distribution at t = {n*dt:.3f} s')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

# Final plot
plt.figure(figsize=(8, 6))
plt.imshow(u, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot')
plt.colorbar(label='Temperature')
plt.title('Final Temperature Distribution')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
'''