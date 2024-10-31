import numpy as np

def function ( y2, y1, y):
    return 

def BVP( BV1, BV2, h, ODE ):
    tRange = np.arange(BV1[0], BV2[0], h)
    y = np.zeros_like(tRange)
    y[0] = BV1[1]
    y[-1] = BV2[1]    
    
    return y