from RK4 import RK4
import numpy as np
import matplotlib.pyplot as plt


def F(t, y1, y2):
    return 0

def f1(t, y1, y2):
    return y2

def f2(t, y1, y2):
    c = 5
    m = 20
    k = 20
    sign = np.sign((-c*y2 - k*y1 + F(t, y1, y2))/m)
    return np.sqrt(np.abs((-c*y2 - k*y1 + F(t, y1, y2))/m))*sign

def f3(t, y1, y2):
    c = 40
    m = 20
    k = 20
    sign = np.sign((-c*y2 - k*y1 + F(t, y1, y2))/m)
    return np.sqrt(np.abs((-c*y2 - k*y1 + F(t, y1, y2))/m))*sign

def f4(t, y1, y2):
    c = 200
    m = 20
    k = 20
    sign = np.sign((-c*y2 - k*y1 + F(t, y1, y2))/m)
    return np.sqrt(np.abs((-c*y2 - k*y1 + F(t, y1, y2))/m))*sign

fu = [f1, f2]
fc = [f1, f3]
fo = [f1, f4]
t0 = 0
y0 = [1, 0]
tRange, y1 = RK4(0, y0, fu, 0.1, 15)
tRange, y2 = RK4(0, y0, fc, 0.1, 15)
tRange, y3 = RK4(0, y0, fo, 0.1, 15)



plt.figure()
plt.plot(tRange, y1[:, 0], label='underdamped')
plt.plot(tRange, y2[:, 0], label='critically damped')
plt.plot(tRange, y3[:, 0], label='overdamped')
plt.title('Mass spring damper system')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
