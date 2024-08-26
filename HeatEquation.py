import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import seaborn as sns
import random
import math
from enum import Enum

class PrescribedBoundaries(Enum):
    FLUX = 1
    TEMPERATURE = 2
    NEWTONIAN = 3

t = 0          # Simulation time
dt = 0.1       # Time step
alpha = .9     # Thermal constant
Q = 10         # Heat production
boundaryConditions = [PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE]

def fill_2d_array(rows, cols, min_value=0, max_value=100):
    # Create a 2D array (list of lists) filled with random values
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((random.random() * (max_value - min_value) + min_value))
        array.append(row)
    return np.array(array)

def plot_heatmap(data, title="Temperature", cmap="viridis", annot=False):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=annot, cmap=cmap)
    plt.title(title)
    plt.show()

def forcing_function(data):
    # Use the 2D heat equation: du/dt = alpha * (d^2h/dx^2 + d^2h/dy^2)
    tempChange = np.zeros_like(data)
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            tempChange[i][j] = alpha * approx_laplacian(data, i, j)
            '''
            if( i in range(45, 55)):
                tempChange[i][j] += 5
            '''
    return tempChange

def gaussian_2d(x, y):
    r = math.sqrt((x-50)**2 + (y-50)**2)
    return math.e**(-.001 * r**2)

def approx_laplacian(data, x, y):
    dx1 = data[x][y] - data[x - 1][y]
    dx2 = data[x + 1][y] - data[x][y]
    ddx = dx2 - dx1
    
    dy1 = data[x][y] - data[x][y - 1]
    dy2 = data[x][y + 1] - data[x][y]
    ddy = dy2 - dy1
    
    return ddx + ddy

def animate(i):
    update_heat(random_array)
    ax.clear()
    sns.heatmap(random_array, cmap="coolwarm", cbar=False, ax=ax, annot=False)

def update_heat(data):
    global t
    t += dt
    data += forcing_function(data) * dt
    boundary_conds_update(data)

def boundary_conds_update(data):
    for i in range(len(boundaryConditions)):
        if boundaryConditions[i] == PrescribedBoundaries.FLUX:
            boundaryFunction = flux_boundary
        elif boundaryConditions[i] == PrescribedBoundaries.TEMPERATURE:
            boundaryFunction = temperature_boundary
        elif boundaryConditions[i] == PrescribedBoundaries.NEWTONIAN:
            boundaryFunction = newtonian_boundary

        if i == 0:
            for y in range(len(data)):
                boundaryFunction(data, y, 0)
        elif i == 1:
            for x in range(len(data[0])):
                boundaryFunction(data, 0, x)
        elif i == 2:
            for y in range(len(data)):
                boundaryFunction(data, y, len(data[0]) - 1)
        elif i == 3:
            for x in range(len(data[0])):
                boundaryFunction(data, len(data) - 1, x)

def flux_boundary(data, x, y):
    flux_rate = 10
    data[x][y] -= flux_rate

def temperature_boundary(data, x, y):
    temp = 60
    data[x][y] = temp

def newtonian_boundary(data, x, y):
    outer_temp = 10
    alpha2 = 2  # Thermal conductivity
    data[x][y] += (outer_temp - data[x][y]) * alpha2 * dt

# Example usage
rows = 100
cols = 100
min_value = 1
max_value = 100

random_array = fill_2d_array(rows, cols, min_value, max_value)
fig, ax = plt.subplots(figsize=(10, 8))
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()
