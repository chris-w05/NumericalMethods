# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:38:02 2024

@author: clark
"""
import numpy as np

def pathogen_spread(E, I, t_index, Iact, U, V, M_max, farm):
    """
    Vectorized pathogen spread update to increase efficiency.
    """
    # Calculate wind speed and factor
    wind_speed = np.sqrt(U[t_index]**2 + V[t_index]**2)
    factor = farm['eta'] * wind_speed / M_max
    wdir = np.arctan2(U[t_index], V[t_index])

    # Calculate directional offsets for wind direction
    crit_value = np.cos(np.deg2rad(67.5))
    cos = np.cos(wdir)
    sin = np.sin(wdir)
    i_offset = np.sign(cos) * (np.abs(cos) >= crit_value)
    j_offset = np.sign(sin) * (np.abs(sin) >= crit_value)

    # Indices of active infections
    infected_indices = np.where(Iact)

    # Update E array based on wind direction and infection
    for i, j in zip(*infected_indices):
        i_ind = int(np.clip(i + i_offset, 0, farm['NpX'] - 1))
        j_ind = int(np.clip(j + j_offset, 0, farm['NpY'] - 1))
        E[i_ind, j_ind, t_index - 1] += factor * I[i, j, t_index - 1]

    return E