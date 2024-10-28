import numpy as np
import matplotlib.pyplot as plt

def dydt(t, y, z):
    return -2*y + 4*np.e**(-t)

def dzdt(t, y, z):
    return -y*z**2/3

def solveSystemEulers( functions, y0, z0, t0, tf, h ):
    tRange = np.arange(t0, tf, h )
    y = np.zeros_like(tRange)
    z = np.zeros_like(tRange)
    for i in range( 1, len(tRange) ):
        y[i] = y[i-1] + functions[0]( tRange[i-1], y[i-1], z[i-1]) * h
        z[i] = z[i-1] + functions[1]( tRange[i-1], y[i-1], z[i-1]) * h
    
    return y, z, tRange

y, z, tRange = solveSystemEulers( [dydt, dzdt] , 2, 4, 0, 1, .1)


def RK4(t0, y0, f, h, tf):
    tRange = np.arange(t0, tf, h)
    y = np.zeros((len(tRange), len(y0)))
    y[0] = y0
    k = np.zeros((len(y0), 4))

    for i, t in enumerate(tRange[:-1]): 
        k[:, 0] = h * np.array([f_i(t, *y[i]) for f_i in f])
        k[:, 1] = h * np.array([f_i(t + h / 2, *(y[i] + k[:, 0] / 2)) for f_i in f])
        k[:, 2] = h * np.array([f_i(t + h / 2, *(y[i] + k[:, 1] / 2)) for f_i in f])
        k[:, 3] = h * np.array([f_i(t + h, *(y[i] + k[:, 2])) for f_i in f])
        y[i + 1] = y[i] + (k[:, 0] + 2 * k[:, 1] + 2 * k[:, 2] + k[:, 3]) / 6

    return tRange, y


plt.figure()
plt.plot( tRange, y)
plt.title('Y over time')
plt.ylabel('Y')
plt.xlabel('t')
plt.figure()
plt.plot( tRange, z)
plt.title('Z over time')
plt.ylabel('Z')
plt.xlabel('t')
plt.show()
