import numpy as np
import matplotlib.pyplot as plt

def ball_motion(t, y, params):
    """
    Input Arguments:
        • t (scalar): Current time.
        • y (scalar): Velocity of the falling ball at time t.
        • params (array): Array of system properties
        - params(1): Gravity
        - params(2): Air density
        - params(3): Ball Mass
        - params(4): Ball radius
        - params(5): Drag coefficient
    Output Arguments:
        • dydt (scalar): The f(t,y) from y'= f(t,y) evaluated at time t.
    """
    rho = params['Air_density']
    Cd = params['Drag_coefficient']
    A = np.pi * params['Ball_radius']**2
    drag_force = .5*(rho*Cd*A*y**2)
    return params['Gravity'] - drag_force/params['Ball_mass']

def euler(odefun, tspan, y0):
    """
    Input Arguments:
        • odefun (callable) - Function to solve. The function dydt = odefun(t,y), for a scalar t and a
        scalar y, must return a scalar dydt that corresponds to f(t,y). odefun must accept both input
        arguments t and y, even if one of the arguments is not used in the function.
        • tspan (array) - Time values of integration. The elements in tspan must be all increasing.
        The solver imposes the initial conditions given by y0 at the initial time given in the βirst entry of
        tspan, then integrates from the βirst to the last entry in tspan.
        • y0 (scalar) - Initial conditions. y0 contains the initial condition for the equation deβined in
        odefun.
    Output Arguments:
        • t (array) - Evaluation points. t is the same as tspan.
        • y (array) - Solution returned as an array. Each row in y corresponds to the solution at the value
        returned in the corresponding row of t.
    """
    tprev = tspan[0]
    y = np.zeros_like(tspan)
    y[0] = y0
    for i in range(1, len(tspan)):
        t = tspan[i]
        h = t - tprev
        y[i] = y[i-1] + odefun(t, y[i-1], params)*h
        tprev = t
    return tspan, y

#Script body---------------------------------------------------------------------------

params = {
    'Gravity': 9.81,            #m/s^2
    'Air_density': 1.255,       #kg/m^3 
    'Ball_mass': 1,             #kg
    'Ball_radius': .05,         #m
    'Drag_coefficient': .4      #unitless
}


tspan = np.linspace(0, 100, 10000)
t, y = euler(ball_motion, tspan, 1)

plt.figure()
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.title('Velocity over time for falling object')
plt.show()


#My numerical results look reasonable because the velocity starts at my initial condition, and accelerates with
#an acceleration of about g. As the object picks up speed, the acceleration decreases - this fits my conceptual
#model because the drag force will counter the force of gravity. As t -> infinity, the velocity of the object 
#approaches an equilibrium velocity where the drag force is equivalent to gravitational force and there will be no acceleration. 