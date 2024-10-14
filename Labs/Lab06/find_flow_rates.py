import numpy as np
import pandas as pd
from naive_gauss import naive_gauss_elimination
#calls naive_gauss_elimination

#determines five unknown flow rates
dP0 = 100*1e3        #kPa
mu = 1e-3           #Ns/m^2
rho = 1e3           #kg/m^3
g = 9.81            #m/s^2

#pipedata dictionary
pipedata = {
    'AB' : {'l' : 5, 'D' : .01, 'R': None, 'F':0, 'Re':None},
    'BG' : {'l' : 5, 'D' : .005, 'R': None, 'F':0, 'Re':None},
    'CF' : {'l' : 5, 'D' : .002, 'R': None, 'F':0, 'Re':None},
    'DE' : {'l' : 5, 'D' : .003, 'R': None, 'F':0, 'Re':None},
    'BC' : {'l' : 10, 'D' : .005, 'R': None, 'F':0, 'Re':None},
    'CD' : {'l' : 10, 'D' : .0035, 'R': None, 'F':0, 'Re':None},
    'EF' : {'l' : 10, 'D' : .0025, 'R': None, 'F':0, 'Re':None},
    'FG' : {'l' : 10, 'D' : .0045, 'R': None, 'F':0, 'Re':None}
}

#Find fluid resistance and add it to dictionary
def fluid_resistance(mu, pipedata, g=9.81):
    for pipe in pipedata.items():
        l = pipe['l']
        D = pipe['D']
        R = 128*mu*l/(np.pi * D**4)
        pipe['R'] = R
    return pipedata 

#Reynolds function to find whether fluid is turbulent or not
def reynolds( V, D):
    '''
    Params
        V: velocity
        D: diameter
    '''
    return rho*V*D/mu

#Script body: ----------------------------------------------------------------------------------
#Find fluid resistance for each pipe
fluid_resistance(mu, pipedata)

#System of equations for flow rates
systemA = [
    [1, -1, -1, 0 ,0],
    [0, 1, 0, -1, -1],
    [pipedata['AB']['R'] -pipedata['AB']['R'], 0, pipedata['BG']['R'], 0 ,0],
    [0, -pipedata['BC']['R']-pipedata['FG']['R'], pipedata['BG']['R'], -pipedata['CF']['R'], 0],
    [0, 0, 0, pipedata['CF']['R'], -(pipedata['CD']['R'] + pipedata['DE']['R'] + pipedata['EF']['R'])]
]

#B side of system of equations
systemB = [0, 0, dP0, 0, 0]

#Solve system of equations using naive gauss eliminaiton
pipes = ['AB', 'BC', 'BG', 'CF', 'DE'] # = [Q0, Q1, Q2, Q3, Q4]
flow_rates = naive_gauss_elimination(systemA, systemB)
for i in range(0, len(pipes)):
    pipedata[pipes[i]]['F'] = flow_rates[i]
    
#Manually assigning flow rates for 3 pipes outside of system of equations
pipedata['EF']['F'] = pipedata['DE']['F']
pipedata['CD']['F'] = pipedata['DE']['F']
pipedata['FG']['F'] = pipedata['EF']['F'] + pipedata['CF']['F']


#displaying flow rates
pipesFlows = {
    ('Pipe') : pipes,
    ('Flow rate'): flow_rates
}
df0 = pd.DataFrame(pipedata)
print(df0)

#Finding reynolds numbers and reporting if they are turbulent
all_pipes = ['AB', 'BG', 'CF', 'DE', 'BC', 'CD', 'EF', 'FG']
reynolds_numbers = np.zeros(8)
for i in range(0, len(all_pipes)):
    D = pipedata[all_pipes[i]]['D']
    V = pipedata[all_pipes[i]]['F'] / (np.pi * (D/2)**2)  # Velocity
    reynolds_numbers[i] = reynolds(V, D)
    pipedata[all_pipes[i]]['Re'] = reynolds(V,D)
    
    # Check if flow is turbulent
    if reynolds_numbers[i] > 2000:
        print(f'Turbulent flow detected in pipe {all_pipes[i]} (Re = {reynolds_numbers[i]:.2f})')

#Displaying final data

df = pd.DataFrame(pipedata)
print(df)