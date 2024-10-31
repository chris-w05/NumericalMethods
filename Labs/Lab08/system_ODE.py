import numpy as np

def system_ODE( t, population):
    P = population[0]
    S = population[1]
    L = population[2]
    I = population[3]
    R = population[4]
    beta = .4       #transmission rate of disease: plants/time
    e = .3          #mu of infection from external sources
    muL = .2        #length of time before latent population becomes susceptible 1/latent period
    k = .5          #rate of plant growth
    Tmin = 10       #min temperature for plants to grow
    Tmax = 35       #max temp for plants to grow
    T = 25          #deg C, constant for this sim
    Tunit = T-Tmin if Tmin < T & Tmax > T else 0
    dPdt = k*Tunit
    dSdt = -(beta*S*I + e) + dPdt
    dLdt = (beta*S*I + e) - muL**-1 * L
    dIdt = muL**-1 * L - muL**-1*I
    dRdt = muL**-1 * I
    #return output of th e
    return [dPdt, dSdt, dLdt, dIdt, dRdt]
