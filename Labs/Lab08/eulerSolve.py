import numpy as np


def euler( system, intial_conditions, params, pop_params):
    '''
    Input Arguments:
        - system: Function hand that returns an array of derivatives
        - intial_conditions: Initial conditions of dependent variables
        - params: time parameters
    '''
    h = params[2]
    t_range = np.arange(params[0], params[1], h)
    #States structrure: rows: (S, L, I, R, P) columns: time steps
    states = np.zeros((len(intial_conditions), len(t_range)))
    states[:,0] = intial_conditions
    
    #Iterate through functions to solve for next state
    for i in range( len(t_range) - 1):
        states[:,i+1] = states[:,i] + np.multiply( h, system(t_range[i], states[:,i], pop_params))
    
    return states, t_range
