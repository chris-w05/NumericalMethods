"""
2450 lab group
pathogen spread function
"""
import numpy as np
from rk4 import rk4
from pathogen_spread import pathogen_spread
from SLIRPE import SLIRPE_Model
from multiprocessing import Pool
import time

def pathogen_growth_2D(S,L,I,R,P,E,lsl,T,Tmin,Tmax,U,V,times,farm, print_times=True, print_updates=True):
    """
    Computes the increase in incidence of a plant pathogen (or any pathogen
with stationary hosts) in 2D for a given set of initial conditions, pathogen and host growth
parameters, farm parameters, and environmental conditions.

    Inputs:
     Initial values of SLIRPE variables and parameters, Environmental forcing
     (U,V,T, T min , T max ), number of plants in the X direction NpX, number of vines in the Y
     direction NpY, number of time steps Nsteps
    Outputs:
      - SLIPE: all SLIRPE variables
    """
    #transmission threshold
    threshold = .00001
    
    #Setting M_max to larger of either component - not certain this is right
    U_max = np.max(U)
    V_max = np.max(V)
    M_max = np.sqrt(U_max**2 + V_max**2)

    #Set params beeded for SLIRPE into an array
    beta = farm['beta']
    mu_L = farm['mu_L'] 
    mu_I = farm['mu_I'] 
    k = farm['k']
    params = [beta,mu_L,mu_I,k,T,Tmin,Tmax]
    
    #declare function handle
    odefun = lambda t,y: SLIRPE_Model(t, y, params) 
    '''
    Start time loop
     Update list of plantsI active that are actively spreading infection (Infectious
     if plants are active call PathogenSpread() to find transmission rate to impacted plants
    ''' 
    
    if print_times:
        print('Starting time loop')
        start_time = time.time()
        
    for t, current_time in enumerate(times[:-1], start=1):

        #check if any plany is infectious
        if np.any(lsl):
            E = pathogen_spread( E,I,t,lsl,U,V,M_max,farm)
        
        #trying a vector-vise operation - all x and y indexes at once
        y0 = [S[:,:,t-1], L[:,:,t-1] , I[:,:,t-1], R[:,:,t-1], P[:,:,t-1], E[:,:,t-1]]
        
        # find new values for all cells
        y = rk4(odefun, current_time, farm['dt'], y0)
        
        #Taking all x and y values from populations to be computed as a vector-wise operation
        [S[:,:,t], L[:,:,t] , I[:,:,t], R[:,:,t], P[:,:,t], E[:,:,t]] = y
        
        #update infectious cells
        lsl = I[:, :, t] >= threshold
        
        #optionally print updates every 20 iterations
        if print_updates and current_time % 10 < farm['dt']/2:
            count_infected = np.count_nonzero(lsl)
            print(f't = {current_time:3.0f}, number infected = {count_infected}')
    
    if print_times:
        stop_time = time.time()
        print(f'Simulation complete in {stop_time - start_time:3.2f} seconds')

    #return SLIRPE values
    return S,L,I,R,P,E