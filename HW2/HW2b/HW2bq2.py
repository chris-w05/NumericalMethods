import math
import numpy as np


P0 = 88113          #pascals
P1 = P0 + 344738    #pascals
r = .1143           #meters
h = .55             #meters
#Errors
dr = .0254          #meters
dh = .0254          #meters
dP0 = 16.93194      #pascal
dP1 = 13789.5       #pascal 
    
def errorV(r, h, dr, dh):
    return [np.abs(math.pi * ( 2*r*h*dr)) , 
            np.abs(math.pi * r**2 * dh) ]

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
    gradP0 = np.abs((V - (P1*V)/P0) * dP0)
    gradP1 = np.abs((V * math.log(P1/P0)) * dP1)
    gradh , gradr = errorV(r,h,dr, dh)
    gradV = np.abs((P1 * math.log(P1/P0) + P0 - P1) * (gradh + gradr))
    print(f'Error from p0: {gradP0:.5} Joules \nError from P1: {gradP1:.5} Joules')
    print(f'Error from V: {gradV:.5} Joules')
    print(f'Volume Errors:\n\tError from r: {gradr:.5} m^3\n\tError from h: {gradh:.5} m^3')
    return gradP0 + gradP1 + gradV

print(f'Total error: {error(P0, P1, r, h, dP0, dP1, dr, dh):.5} Joules' )
# Taking these results, the largest error is from the measurements on the tank, mainly because errors are compounded
# when the volume is found, and then further compounded when used in the energy equation
#Because the largest source of error is from the measurement of the volume of the tank, additional pressure
#sensors are unlikely to be worthwhile
