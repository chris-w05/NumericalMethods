import math
import numpy as np


P0 = 88113          #pascals
P1 = P0 + 344738    #pascals
r = .1143           #meters
h = .55             #meters
dr = .0254          #meters
dh = .0254          #meters
dP0 = 33.8639       #pascal
dP1 = 13789.5       #pascal 
    
def errorV(r, h, dr, dh):
    return math.pi * ( 2*r*h*dr + r**2 * dh )

def error(P0, P1, r, h, dP0, dP1, dr, dh):
    """
    Arguments:
        P0 (Pascals) : Pressure outside tank
        P1 (Pascals) : Pressure insite tank
        r (meters): Radius of tank
        h (meters): Height of tank
        dP0 (Pascals) : Pressure uncertainty outside tank
        dP1 (Pascals): Pressure uncertainty inside tank
        dr (meters): Radius uncertainty
        dh (meters): Height uncertainty
    """
    V = math.pi * r**2 * h
    gradP0 = (V - (P1*V)/P0) * dP0
    gradP1 = V * math.log(P1/P0) * dP1
    gradV = (P1 * math.log(P1/P0) + P0 - P1) * errorV(r,h,dr, dh)
    print(f'Error from p0: {gradP0}\nError from P1: {gradP1}\nError from V: {gradV}')
    return gradP0 + gradP1 + gradV

error(P0, P1, r, h, dP0, dP1, dr, dh )
# Taking these results, the largest error is from the measurements on the tank