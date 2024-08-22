import math
import matplotlib.pyplot as plt
import numpy as np

t = 0           #time s
y = 2           #water level m
A = 850         #Area, m^2
Q = 325         #flow rate m^3/2
alpha = 200     #constant m^3/2 / s
h = .5          #step size s
maxTime = 10    #simulation limit s

#Store values to be produced then plotted from euler's
time_values = []
y_values = []

#defines dy/dt 
def forcingfunc(time, ylevel):
    return 2 * (Q/A) * math.sin(time)**2  - ((alpha)/A * ((1 + ylevel)**(3/2)))

#loop through estimations
while t < maxTime:
    #print("Time: %2f, Y-level: %f " % (t, y))
    time_values.append(t)
    y_values.append(y)
    y = y + forcingfunc(t, y)*h
    t += .5

#appending last time
time_values.append(t)
y_values.append(y)
#print("Time: %2f, Y-level: %f " % (t, y))   


# Plotting the water level over time
plt.figure(figsize=(8, 6))
plt.plot(time_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Water Level Over Time Using Euler\'s Method')
plt.xlabel('Time (s)')
plt.ylabel('Water Level (m)')
plt.grid(True)
plt.show()
