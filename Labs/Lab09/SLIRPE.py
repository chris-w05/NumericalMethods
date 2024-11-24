# -*- coding: utf-8 -*-
"""
2450 lab project
SLIRPE function
"""
import numpy as np
def SLIRPE_Model(t,y,params):
    """
    A function that solves for all slopes of inputs and
    can be used as an input argument into RK4 function
    Inputs:
    • t = a time input index that tracks which time iteration you are on to iterate the temperature forcing
    • y = a vector for each of the primary variables in Equation (1)
    • params = all parameters required to evaluate Equation (1) including:
        • beta_max = the max rate of colony growth/new infections
        • mu_L = the inverse of the instantaneous latent period calculated using Equation (9)
        • mu_I = the inverse of the duration of the infectious period (a constant)
        • K = the rate of new infections from external sources (a constant)
        • T = an array of air temperature
        • 𝑇_min = a scalar value that sets the minimum temperature for plant growth
        • T_max = a scalar value that sets the maximum temperature for plant growth
    """
    
    #index out
    S = y[0]
    L = y[1]
    I = y[2]
    R = y[3]
    E = y[5]
    beta = params[0]
    mu_L = params[1]
    mu_I = params[2]
    k = params[3]
    T = params[4]
    T_min = params[5]
    T_max = params[6]
    
    T = T[0]
    #calculate T unit:
    #since the time index is not being passed into SPIRPE, and temperatures are constant 
    #im setting the temperature to always be that of index 0
    if T_min<T and T<T_max:
        T_unit = T-T_min
    elif T<T_min or T_max<T:
        T_unit = 0
     
      
    dEdt = E   
    dPdt = k * T_unit + dEdt #total population 
    dSdt = -1*(beta*S*I + dEdt) + dPdt #susceptible population
    dLdt = (beta*S*I + dEdt) - (L/mu_L)#latent population
    dIdt = L/mu_L - I/mu_I #infected population
    dRdt = I/mu_I #removed(dead or recovered)
    dydt = np.array(([dSdt,dLdt,dIdt,dRdt,dPdt,dEdt]))

    return dydt

