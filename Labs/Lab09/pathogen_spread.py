# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:38:02 2024

@author: clark
"""
import numpy as np

def pathogen_spread(E, I, t_index, Iact, U, V, M_max, farm):
    """
    Inputs:
        - E: external pathogen spread rate
        - I: Infected fraction
        - t_index: current time index
        - Iact (2D array): where infections are happening
        - U: Wind component
        - V: Wind component
        - M_max: Maximum windspeed
        - farm: Farm configuration dictionary
    Outputs:
        - Updated E array with rates for SLIRPE
    """
    # Find indices of active infections
    li, ji = np.where(Iact > 0)
    
    # Calculate transmission factor and wind direction
    wind_speed = np.sqrt(U[t_index]**2 + V[t_index]**2)
    factor = farm['eta'] * wind_speed / M_max
    wdir = np.arctan2(V[t_index], U[t_index])

    # Determine infection spread direction offsets based on wind direction
    # see chart of wind direction v spread 
    crit_value = np.cos(np.deg2rad(67.5))
    cos = np.cos(wdir)
    sin = np.sin(wdir)
    i_plus = int( np.abs(cos)  >= crit_value) * int(np.sign(cos))
    j_plus = int( np.abs(sin)  >= crit_value) * int(np.sign(sin))

    #speed up loop:
    # Vectorized calculation of neighbor indices
    i_ind = li + i_plus
    j_ind = ji + j_plus
    # Apply boundary conditions using np.clip
    i_ind = np.clip(i_ind, 0, farm['NpX'] - 1)
    j_ind = np.clip(j_ind, 0, farm['NpY'] - 1)
    
    # Vectorized calculation of external transmission rate
    E[i_ind, j_ind, t_index - 1] = factor * I[li, ji, t_index - 1]
    
    return E
