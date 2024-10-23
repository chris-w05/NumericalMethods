import numpy as np
import matplotlib.pyplot as plt

def RK4(t0, y0, f, h, tf):
    tRange = np.arange(t0, tf, h)
    y = np.zeros((len(tRange), len(y0)))
    y[0] = y0
    k = np.zeros((len(y0), 4))

    for i, t in enumerate(tRange[:-1]):
        for j in range(len(y0)):
            k[j, 0] = h * f[j](t, *y[i])
        for j in range(len(y0)):
            k[j, 1] = h * f[j](t + h / 2, *(y[i] + k[:, 0] / 2))
        for j in range(len(y0)):
            k[j, 2] = h * f[j](t + h / 2, *(y[i] + k[:, 1] / 2))
        for j in range(len(y0)):
            k[j, 3] = h * f[j](t + h, *(y[i] + k[:, 2]))

        y[i + 1] = y[i] + (k[:, 0] + 2*k[:, 1] + 2*k[:, 2] + k[:, 3]) / 6

    return tRange, y

def f1(t, y1, y2):
    return y1 - y2

def f2(t, y1, y2):
    return y1 * y2

f = [f1, f2]
t0 = 0
y0 = [2, 3]
tRange, y = RK4(t0, y0, f, 0.001, 1)
zz