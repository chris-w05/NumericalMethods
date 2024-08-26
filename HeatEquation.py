import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import seaborn as sns
from enum import Enum

class PrescribedBoundaries(Enum):
    FLUX = 1
    TEMPERATURE = 2
    NEWTONIAN = 3

t = 0          # Simulation time
dt = 0.1       # Time step
alpha = 2      # Thermal constant
Q = 10         # Heat production
boundaryConditions = [PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE ]

def fill_2d_array(rows, cols, min_value=0, max_value=100):
    return np.random.uniform(min_value, max_value, (rows, cols))

def plot_heatmap(data, title="Temperature", cmap="viridis", annot=False):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=annot, cmap=cmap)
    plt.title(title)
    plt.show()

def forcing_function(data):
    tempChange = np.zeros_like(data)
    # Compute Laplacian for all cells, including boundaries
    tempChange += alpha * approx_laplacian(data) -.05
    return tempChange

def approx_laplacian(data):
    # Laplacian calculation with consideration of boundaries
    laplacian = np.zeros_like(data)
    
    # Interior
    laplacian[1:-1, 1:-1] = (
        np.roll(data, -1, axis=0)[1:-1, 1:-1] + 
        np.roll(data, 1, axis=0)[1:-1, 1:-1] +
        np.roll(data, -1, axis=1)[1:-1, 1:-1] + 
        np.roll(data, 1, axis=1)[1:-1, 1:-1] - 
        4 * data[1:-1, 1:-1]
    )
    
    # Edges (simplified for clarity)
    laplacian[0, 1:-1] = data[1, 1:-1] + data[0, :-2] + data[0, 2:] - 3 * data[0, 1:-1]
    laplacian[-1, 1:-1] = data[-2, 1:-1] + data[-1, :-2] + data[-1, 2:] - 3 * data[-1, 1:-1]
    laplacian[1:-1, 0] = data[1:-1, 1] + data[:-2, 0] + data[2:, 0] - 3 * data[1:-1, 0]
    laplacian[1:-1, -1] = data[1:-1, -2] + data[:-2, -1] + data[2:, -1] - 3 * data[1:-1, -1]
    
    # Corners
    laplacian[0, 0] = data[0, 1] + data[1, 0] - 2 * data[0, 0]
    laplacian[0, -1] = data[0, -2] + data[1, -1] - 2 * data[0, -1]
    laplacian[-1, 0] = data[-2, 0] + data[-1, 1] - 2 * data[-1, 0]
    laplacian[-1, -1] = data[-1, -2] + data[-2, -1] - 2 * data[-1, -1]
    
    return laplacian

def gaussian_2d(data):
    array = np.zeros_like(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            r = np.sqrt( (i - len(data)/2)**2 + (j - len(data[i])/2)**2)
            array[i][j] = np.e**(-(.1*r)**2)
    return array

def update_heat(data):
    global t
    dt = .1 * np.e**(.001*t)
    t += dt
    data += forcing_function(data) * dt
    boundary_conds_update(data)

def boundary_conds_update(data):
    boundary_funcs = {
        PrescribedBoundaries.FLUX: flux_boundary,
        PrescribedBoundaries.TEMPERATURE: temperature_boundary,
        PrescribedBoundaries.NEWTONIAN: newtonian_boundary,
    }

    for i, boundaryCondition in enumerate(boundaryConditions):
        boundaryFunction = boundary_funcs[boundaryCondition]

        if i == 0:  # Left
            for y in range(len(data)):
                boundaryFunction(data, y, 0)
        elif i == 1:  # Top
            for x in range(len(data[0])):
                boundaryFunction(data, 0, x)
        elif i == 2:  # Right
            for y in range(len(data)):
                boundaryFunction(data, y, len(data[0]) - 1)
        elif i == 3:  # Bottom
            for x in range(len(data[0])):
                boundaryFunction(data, len(data) - 1, x)

def flux_boundary(data, x, y):
    flux_rate = 0.05
    data[x, y] -= flux_rate

def temperature_boundary(data, x, y):
    temp = 0
    #specific boundary temperatures
    if( x < 1):
        temp = 60
    if( y < 1):
        temp = 10
    if(x > len(data) - 2):
        temp = 60
    if(y > len(data[x] - 2)):
        temp = 10
    data[x, y] = temp

def newtonian_boundary(data, x, y):
    outer_temp = 10
    alpha2 = 2  # Thermal conductivity
    data[x, y] += (outer_temp - data[x, y]) * alpha2 * dt

def animate(i):
    update_heat(random_array)
    ax.clear()
    sns.heatmap(random_array, cmap="coolwarm", cbar=False, ax=ax, annot=False)

# Example usage
rows, cols = 100, 100
random_array = fill_2d_array(rows, cols)
fig, ax = plt.subplots(figsize=(10, 8))
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()
