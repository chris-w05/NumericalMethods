import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
<<<<<<< Updated upstream
import seaborn
import random
import math
=======
import seaborn as sns
>>>>>>> Stashed changes
from enum import Enum

class prescribed_boundaries(Enum):
    flux = 1
    temperature = 2
    newtonian = 3

<<<<<<< Updated upstream
t = 0           #simulation time
dt = .5        #time step
alpha = 10  #thermal constant
Q = 100        #Heat production
boundaryConditions = [prescribed_boundaries.temperature, prescribed_boundaries.temperature, prescribed_boundaries.temperature, prescribed_boundaries.temperature]

def fill_2d_array(rows, cols, min_value=0, max_value=100):
    # Create a 2D array (list of lists) filled with random values
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((random.random() * (max_value - min_value) + min_value) )
        array.append(row)
    return np.array(array)
=======
t = 0          # Simulation time
dt = 0.1       # Time step
alpha = 2      # Thermal constant
Q = 10         # Heat production
boundaryConditions = [PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE, PrescribedBoundaries.TEMPERATURE ]

def fill_2d_array(rows, cols, min_value=0, max_value=100):
    return np.random.uniform(min_value, max_value, (rows, cols))
>>>>>>> Stashed changes

def plot_heatmap( data, title = "Temperature", cmap="inferno", annot=False ):
    plt.figure(figsize=(10, 8))
    seaborn.heatmap(data, annot=annot, cmap=cmap,)
    plt.title(title)
    plt.show()
<<<<<<< Updated upstream
    
def forcing_function(data, time):
    #use the 2d heat equation: du/dt = a( d^2h/dx^2 + d^2h/dy^2)
    tempChange = np.zeros_like(data)
    for i in range( 1, len(data) - 1):
        for j in range( 1, len(data[i]) - 1):
            if( i > 0 ):
                tempChange[i][j] = approx_laplacian(data, i , j)
    return tempChange
    
def gaussian_2d(x, y):
    r = math.sqrt( x**2 + y**2)
    return math.e**( -1 * r**2)

def approx_laplacian(data, x , y):
    dx1 = data[x][y] - data[x - 1][y]
    dx2 = data[x + 1][y] - data[x][y]
    ddx = dx1 - dx2
    
    dy1 = data[x][y] - data[x][y - 1]
    dy2 = data[x][y + 1] - data[x][y]
    ddy = dy1 - dy2
    
    return ddx - ddy
    
  
def animate(i):
    update_heat(random_array)
    ax.clear()
    seaborn.heatmap( random_array, cmap="coolwarm", cbar=False, ax=ax)
    
def update_heat(data):
    global t
    t += dt
    data += forcing_function(data, t )*dt
    boundary_conds_update(data)
    
def boundary_conds_update(data):
    #boundary cond 1: -x
    
    for i in range(len(boundaryConditions)):
        if boundaryConditions[i] == prescribed_boundaries.flux:
            #do something
            boundaryFunction = flux_boundary
        elif boundaryConditions[i] == prescribed_boundaries.temperature:
            #something else
            boundaryFunction = temperature_boundary
        elif boundaryConditions[i] == prescribed_boundaries.newtonian:
            #something else 
            boundaryFunctionn = newtonian_boundary
        
        if i == 0:
            for y in range(0, len(data)):
                boundaryFunction(data, y, 0)
        elif i == 1:
            for x in range(0, len(data[0])):
                boundaryFunction(data, 0, x)
        elif i == 2:
            for y in range(0, len(data)):
                boundaryFunction(data, y, len(data) - 1)
        elif i == 3:
            for x in range(0, len(data[0])):
                boundaryFunction(data, len(data[0]) - 1, x)
        

def flux_boundary(data, x, y):
    flux_rate = 10
    data[x][y] -= flux_rate 

def temperature_boundary(data, x, y):
    temp = 100
    data[x][y] = temp

def newtonian_boundary(data, x, y):
    outer_temp = 50
    alpha2 = .1 #thermal conductivity
    data[x][y] += (outer_temp - data[x][y]) * alpha2 * dt
      
                
# Example usage
rows = 100
cols = 100
min_value = 1
max_value = 10

random_array = fill_2d_array(rows, cols, min_value, max_value)
=======

def forcing_function(data):
    tempChange = np.zeros_like(data)
    # Compute Laplacian for all cells, including boundaries
    tempChange += alpha * approx_laplacian(data)
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
>>>>>>> Stashed changes
fig, ax = plt.subplots(figsize=(10, 8))
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()