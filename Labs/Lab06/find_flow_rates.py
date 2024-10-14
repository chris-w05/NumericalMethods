import numpy as np
import pandas as pd
from naive_gauss import naive_gauss_elimination
#calls naive_gauss_elimination

#determines five unknown flow rates
dP0 = 100*1e3        #kPa
mu = 1e-3           #Ns/m^2
rho = 1e3           #kg/m^3
g = 9.81            #m/s^2

#pipedata dictionary with updated keys
pipedata = {
    'AB' : {'Length': 5, 'Diameter': .01, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'BG' : {'Length': 5, 'Diameter': .005, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'CF' : {'Length': 5, 'Diameter': .002, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'DE' : {'Length': 5, 'Diameter': .003, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'BC' : {'Length': 10, 'Diameter': .005, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'CD' : {'Length': 10, 'Diameter': .0035, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'EF' : {'Length': 10, 'Diameter': .0025, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'FG' : {'Length': 10, 'Diameter': .0045, 'Resistance': None, 'Flow': 0, 'Reynolds': None},
    'GH' : {'Length': 5, 'Diameter': .005, 'Resistance': None, 'Flow': 0, 'Reynolds': None}
}

#Find fluid resistance and add it to the dictionary
def fluid_resistance(mu, pipedata, g=9.81):
    for key, pipe in pipedata.items():
        Length = pipe['Length']
        Diameter = pipe['Diameter']
        Resistance = 128*mu*Length/(np.pi * Diameter**4)
        pipe['Resistance'] = Resistance
    return pipedata 

#Reynolds function to find whether fluid is turbulent or not
def reynolds(V, Diameter):
    return rho*V*Diameter/mu

#Script body: ----------------------------------------------------------------------------------
#Find fluid resistance for each pipe
fluid_resistance(mu, pipedata)

#System of equations for flow rates
systemA = [
    [1, -1, -1, 0 ,0],
    [0, 1, 0, -1, -1],
    [pipedata['AB']['Resistance'] + pipedata['GH']['Resistance'], 0, pipedata['BG']['Resistance'], 0 ,0],
    [0, -pipedata['BC']['Resistance']-pipedata['FG']['Resistance'], pipedata['BG']['Resistance'], -pipedata['CF']['Resistance'], 0],
    [0, 0, 0, pipedata['CF']['Resistance'], -(pipedata['CD']['Resistance'] + pipedata['DE']['Resistance'] + pipedata['EF']['Resistance'])]
]

#B side of system of equations
systemB = [0, 0, dP0, 0, 0]

#Solve system of equations using naive gauss elimination
pipes = ['AB', 'BC', 'BG', 'CF', 'DE'] # = [Q0, Q1, Q2, Q3, Q4]
flow_rates = naive_gauss_elimination(systemA, systemB)
for i in range(0, len(pipes)):
    pipedata[pipes[i]]['Flow'] = flow_rates[i]
    
#Manually assigning flow rates for 3 pipes outside of system of equations
pipedata['EF']['Flow'] = pipedata['DE']['Flow']
pipedata['CD']['Flow'] = pipedata['DE']['Flow']
pipedata['FG']['Flow'] = pipedata['EF']['Flow'] + pipedata['CF']['Flow']
pipedata['GH']['Flow'] = pipedata['FG']['Flow'] + pipedata['BG']['Flow']

# Displaying flow rates
for key, pipe in pipedata.items():
    print(f"Pipe {key} flow rate: {pipe['Flow']:.4} m³/s")

# Finding Reynolds numbers and reporting if they are turbulent
for key, pipe in pipedata.items():
    Diameter = pipe['Diameter']
    V = pipe['Flow'] / (np.pi * (Diameter / 2)**2)  # Velocity
    pipe['Reynolds'] = reynolds(V, Diameter)
    # Check if flow is turbulent
    if pipe['Reynolds'] > 2000:
        print(f'Turbulent flow detected in pipe {key} (Re = {pipe["Reynolds"]:.2f})')

# Displaying final data
df = pd.DataFrame.from_dict(pipedata, orient='index')
print(df)
#I can verify my answer is correct by plugging my values for flow and resistance back into the system of equations 
# and seeing whether or not the left side matches the right side