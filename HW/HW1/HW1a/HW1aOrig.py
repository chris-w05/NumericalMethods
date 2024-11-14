import math
import matplotlib.pyplot as plt
import numpy as np

t = 0           #time s
y = 1           #water level m
alpha = 200     #constant m^3/2 / s
h = .001          #step size s
maxTime = 4    #simulation limit s

#Store values to be produced then plotted from euler's
time_values = []
y_values = []

#defines dy/dt 
def forcingfunc(x,y):
    return .5 * ( -3 * x - 5*y + np.e**np.cos((x*y)))

#loop through estimations
while t < maxTime:
    #print("Time: %2f, Y-level: %f " % (t, y))
    time_values.append(t)
    y_values.append(y)
    y = y + forcingfunc(t, y)*h
    t += h

#appending last time
time_values.append(t)
y_values.append(y)
#print("Time: %2f, Y-level: %f " % (t, y))   


# Plotting the water level over time
plt.figure(figsize=(8, 6))
plt.plot(time_values, y_values, linestyle='-', color='b')
plt.title('Plot of 2y\' +3x +5y = e^(cos(xy))')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
