import numpy as np

def solveSystemEulers( functions, y0, z0, t0, tf, h ):
    tRange = np.arange(t0, tf, h )
    y = np.zeros_like(tRange)
    z = np.zeros_like(tRange)
    
    y[0] = y0
    z[0] = z0
    
    for i in range( 1, len(tRange) ):
        y[i] = y[i-1] + functions[0]( tRange[i-1], y[i-1], z[i-1]) * h
        z[i] = z[i-1] + functions[1]( tRange[i-1], y[i-1], z[i-1]) * h
    
    return y, z, tRange