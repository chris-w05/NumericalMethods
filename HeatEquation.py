import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import seaborn
import random

t = 0           #simulation time
dt = .05        #time step
alpha = 100000     #thermal constant

def fill_2d_array(rows, cols, min_value=0, max_value=100):
    # Create a 2D array (list of lists) filled with random values
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((random.random() * (max_value - min_value) + min_value) )
        array.append(row)
    return np.array(array)

def plot_heatmap( data, title = "Temperature", cmap = "viridis", annot=False ):
    plt.figure(figsize=(10, 8))
    seaborn.heatmap(data, annot=annot, cmap=cmap,)
    plt.title(title)
    plt.show()
    
def forcing_function(data, time):
    #use the 2d heat equation: du/dt = a( d^2h/dx^2 + d^2h/dy^2)
    tempChange = np.zeros_like(data)
    for i in range( 1, len(data) - 1):
        for j in range( 1, len(data[i]) - 1):
            if( i > 0 ):
                tempChange[i][j] = approx_laplacian(data, i , j) + 1000*np.sin(t)
    return tempChange
    
def approx_laplacian(data, x , y):
    dx1 = data[x][y] - data[x - 1][y]
    dx2 = data[x + 1][y] - data[x][y]
    ddx = dx1 - dx2
    
    dy1 = data[x][y] - data[x][y - 1]
    dy2 = data[x][y + 1] - data[x][y]
    ddy = dy1 - dy2
    
    return ddx + ddy
    
  
def animate(i):
    update_heat(random_array)
    ax.clear()
    seaborn.heatmap( random_array, cmap="coolwarm", cbar=False, ax=ax)
    
def update_heat(data):
    global t
    t += dt
    data += forcing_function(data, t )*dt
      
                
# Example usage
rows = 100
cols = 100
min_value = 1
max_value = 10

random_array = fill_2d_array(rows, cols, min_value, max_value)
fig, ax = plt.subplots(figsize=(10, 8))
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()