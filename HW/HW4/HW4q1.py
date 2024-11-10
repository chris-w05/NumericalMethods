import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Euler's method

#Forcing function:

def f(x):
    Q = 450
    A = 1250
    return 3 * (Q/A) * np.sin(x)**2 -(Q/A) 

def eulers( t0, y0, tf, h, function):
    tValues = []
    yValues = [y0]
    guess = y0
    for i in np.arange(t0, tf, h):
        tValues.append(i)
        guess = guess + function(i)*h
        yValues.append(guess)
    tValues.append(tf)
    data = {
        ('Time'): tValues,
        ('Level'): yValues
    }
    return guess, data

final, data = eulers(0, 0, 1, .05, f)
df = pd.DataFrame(data)
print(df)
plt.figure()
plt.plot(data['Time'], data['Level'])
plt.xlabel('Time')
plt.ylabel('Water level')
plt.title('Water level over time, h=.05')
plt.show()

final, data = eulers(0, 0, 1, .001, f)
plt.figure()
plt.plot(data['Time'], data['Level'])
plt.xlabel('Time')
plt.ylabel('Water level')
plt.title('Water level over time, h=.001')
plt.show()