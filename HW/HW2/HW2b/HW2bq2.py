import math
import numpy as np


P0 = 88113.8        #pascals
P1 = P0 + 344737.9  #pascals
r = .1143           #meters
h = .55             #meters
#Errors
dr = .0015875       #meters -> 1/16 in
dh = .0015875       #meters -> 1/16 in
dP0 = 16.93194      #pascal -> .005 inHg
dP1 = 6894.76       #pascal -> 1psi

#Error in Volume (partial derivatives of r and h)
def errorV(r, h, dr, dh):
    #returns partial derivates in terms of r and h
    return [np.abs(math.pi*2*r*h*dr) , 
            np.abs(math.pi * r**2 * dh) ]
    
#exergy formula
def exergy(P0, P1, r, h):
    V = np.pi * r**2 * h
    return P1 * V * (math.log(P1/P0) + (P0/P1) - 1)

def error(P0, P1, r, h, dP0, dP1, dr, dh):
    """
    Arguments:
        P0 (Pascals) : Pressure outside tank
        P1 (Pascals) : Pressure inside tank
        r (meters): Radius of tank
        h (meters): Height of tank
        dP0 (Pascals) : Pressure uncertainty outside tank
        dP1 (Pascals): Pressure uncertainty inside tank
        dr (meters): Radius uncertainty
        dh (meters): Height uncertainty
    """
    V = math.pi * r**2 * h
    #partial derivatives multiplied by errors
    gradP0 = np.abs((V - (P1*V)/P0) * dP0)
    gradP1 = np.abs((V * math.log(P1/P0)) * dP1)
    dVr , dVh = errorV(r,h,dr, dh)
    gradr = np.abs((P1 * math.log(P1/P0) + P0 - P1) * (dVr))
    gradh = np.abs((P1 * math.log(P1/P0) + P0 - P1) * (dVh))
    #printing errors
    print(f'Error from p0: {gradP0:.5} Joules \nError from P1: {gradP1:.5} Joules')
    print(f'Error from r: {gradr:.5} Joules')
    print(f'Error from h: {gradh:.5} Joules')
    print(f'Volume Errors:\n\tError from r: {dVr:.5} m^3\n\tError from h: {dVh:.5} m^3')
    return gradP0 + gradP1 + gradh + gradr

#outputting results
error = error(P0, P1, r, h, dP0, dP1, dr, dh)
print(f'Total error: {error:.5} Joules' )
print(f'Exergy = {exergy(P0, P1, r, h):.5} ± {error:.5} Joules') 


# Since the largest error is from the error in P1 (the pressure inside the tank) it would make sense to invest 
# in better pressure sensors inside the tank.