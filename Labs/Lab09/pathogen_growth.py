"""
2450 lab group
pathogen spread function
"""
import numpy as np
from rk4 import rk4
from pathogen_spread import pathogen_spread
from SLIRPE import SLIRPE_Model
from multiprocessing import Pool
    

def pathogen_growth_2D(S, L, I, R, P, E, lsl, T, T_min, T_max, U, V, times, farm):
    """
    Vectorized version of pathogen growth in 2D to improve efficiency.
    """
    # Transmission threshold
    threshold = 0.00001
    M_max = np.sqrt(np.max(U)**2 + np.max(V)**2)

    # Set parameters needed for SLIRPE into an array
    beta = farm['beta']
    mu_L = farm['mu_L']
    mu_I = farm['mu_I']
    k = farm['k']
    params = [beta, mu_L, mu_I, k, T, T_min, T_max]

    # Define ODE function handle for vectorized operations
    def odefun(t, y):
        return SLIRPE_Model(t, y, params)
    
    print('Starting time loop')
    for t, current_time in enumerate(times[:-1], start=1):
        # Update E matrix with pathogen spread if there are any infectious cells
        if np.any(lsl):
            E = pathogen_spread(E, I, t, lsl, U, V, M_max, farm)

        # Collect initial conditions for all cells at once
        y0 = np.stack((S[:, :, t-1], L[:, :, t-1], I[:, :, t-1], R[:, :, t-1], P[:, :, t-1], E[:, :, t-1]), axis=2)

        # Apply rk4 integration on all cells in a vectorized manner
        y_next = np.apply_along_axis(lambda y: rk4(odefun, current_time, farm['dt'], y), 2, y0)

        # Update each state variable
        S[:, :, t], L[:, :, t], I[:, :, t], R[:, :, t], P[:, :, t], E[:, :, t] = y_next.transpose(2, 0, 1)

        # Update infectious status based on threshold
        lsl = I[:, :, t] >= threshold

    return S, L, I, R, P, E