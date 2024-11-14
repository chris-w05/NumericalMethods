
"""
2450 lab group
rk4 function
"""


def rk4(odefun,current_time,dt,y0):  
    """  
    •odefun (callable) – Function to solve. The function dydt = odefun(t,y), for an integer t
    (time index) and a vector y, must return a vector dydt having the same shape as y that
    corresponds to 𝑓(𝑡, 𝑦). odefun() must accept both input arguments t and y, even if one of
    the arguments is not used in the function


    •t_index (integer value) – Time index value of integration. The index should correspond to the
    index of the current timestep.

    • dt (scalar) – The timestep or duration of time between two successive integration times.
    The solver imposes the initial conditions given by y0 at the initial time t0 and then
    integrates from t0 to t1=t0+dt. (h value)

    • y0 (vector) - Initial conditions for a given timestep. y0 contains the initial conditions for
    the equation defined in odefun.
    """
    #follow rk4 formula for one round
    k1 = odefun(current_time,y0)
    k2 = odefun(current_time + dt/2, y0 + dt*k1/2)
    k3 = odefun(current_time + dt/2, y0 + dt*k2/2)
    k4 = odefun(current_time + dt, y0 + dt*k3)
    #update y vec with weighted slope
    y = y0 + (k1 + 2*k2 + 2*k3 + k4)*dt/6
    return y
    
