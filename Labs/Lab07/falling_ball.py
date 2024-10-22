import numpy as np
import matplotlib.pyplot as plt

params = {
    'Gravity': 9.81,            #m/s^2
    'Air_density': 1.255,       #kg/m^3 
    'Ball_mass': 1,             #kg
    'Ball_radius': .05,         #m
    'Drag_coefficient': .4     #unitless
}


def ball_motion(t, y, params):
    rho = params['Air_density']
    Cd = params['Drag_coefficient']
    A = np.pi * params['Ball_radius']**2
    drag_force = .5*(rho*Cd*A*y**2)
    return params['Gravity'] - drag_force/params['Ball_mass']

def euler(odefun, tspan, y0):
    tprev = tspan[0]
    y = np.zeros_like(tspan)
    y[0] = y0
    for i in range(1, len(tspan)):
        t = tspan[i]
        h = t - tprev
        y[i] = y[i-1] + odefun(t, y[i-1], params)*h
        tprev = t
    return tspan, y

tspan = np.linspace(0, 100, 10000)
t, y = euler(ball_motion, tspan, 1)

plt.figure()
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.title('Velocity over time for falling object')
plt.show()