import numpy as np
import matplotlib.pyplot as plt

def RK4(t0, y0, f, h, tf):
    tRange = np.arange(t0, tf, h)
    y = np.zeros((len(tRange), len(y0)))  # Store results for all time steps
    y[0] = y0
    k = np.zeros((len(y0), 4))  # Store the four k values for each equation

    for i, t in enumerate(tRange[:-1]):  # Iterate through the time steps
        k[:, 0] = h * np.array([f_i(t, *y[i]) for f_i in f])
        k[:, 1] = h * np.array([f_i(t + h / 2, *(y[i] + k[:, 0] / 2)) for f_i in f])
        k[:, 2] = h * np.array([f_i(t + h / 2, *(y[i] + k[:, 1] / 2)) for f_i in f])
        k[:, 3] = h * np.array([f_i(t + h, *(y[i] + k[:, 2])) for f_i in f])
        y[i + 1] = y[i] + (k[:, 0] + 2 * k[:, 1] + 2 * k[:, 2] + k[:, 3]) / 6  # Update y

    return tRange, y

def F(t, y1, y2):
    return 20*np.sin(t)

def f1(t, y1, y2):
    return y2

def f2(t, y1, y2):
    c = 120
    m = 100
    k = 10
    return (-c*y2 - k*y1 + F(t, y1, y2))/m



f = [f1, f2]
t0 = 0
y0 = [2, 3]
tRange, y = RK4(t0, y0, f, 0.001, 30)

# Plotting the results
plt.plot(tRange, y[:, 0], label='position')
plt.plot(tRange, y[:, 1], label='velocity')
plt.title('Mass spring damper system')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
