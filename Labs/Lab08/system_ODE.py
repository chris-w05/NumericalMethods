import numpy as np

def system_ODE( t, population, params):
    '''
    Input arguments
        - t: current time
        - population: current population stats: [SLIRP]
        - params: [beta, e, muL, muI, k, Tmin, Tmax, T]
    '''
    #Population statistics
    [S, L, I, R, P] = population
    
    #Parameters
    [beta, muL, muI, e, k, Tmin, Tmax, T] = params
    Tunit = T-Tmin if Tmin < T and Tmax > T else 0
    
    #ODEs
    dPdt = k*Tunit
    dSdt = -(beta*S*I + e) + dPdt
    dLdt = (beta*S*I + e) - muL**-1 * L
    dIdt = muL**-1 * L - muI**-1*I
    dRdt = muI**-1 * I
    #return output of th e
    return [ dSdt, dLdt, dIdt, dRdt, dPdt]
