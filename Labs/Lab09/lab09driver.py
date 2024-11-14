# -*- coding: utf-8 -*-
"""
2450 lab group
lab 9 driver
"""
###IMPORTS###
import numpy as np
from pathogen_growth import pathogen_growth_2D
import matplotlib.pyplot as plt
import math
import time
#############

#set sim variables
days = 75#number of days to simulate
dt = 0.05#fraction of a day/timestep
tspan = dt * np.arange(1, int(np.ceil(days / dt)) + 1)
T = 25 * np.ones(int(np.ceil(days / dt)) + 1) #[ambient temp:C]
T_min = 10#[C]
T_max = 35
U_avg=2
sigma_u=1
U = [U_avg + sigma_u * np.sin(2*math.pi*t) for t in tspan]
V_avg = 0
sigma_v = 2
V= [V_avg + sigma_v * np.sin(2*math.pi*t) for t in tspan]

#collect all global parameters into a single term "farm" (dictionary)
farm = {
        #global pathogen params
        'beta' : 2, #infection rate under ideal conditions/1day
        'mu_L': 2, #length of latent period
        'mu_I' : 4, #rate infection clears
        'eta': 0.1, #plant to plant release fraction scale factor
        
        #global plant params
        'LpX': 1,#x-direction physical length of plant[m]
        'LpY':1, #y-direction physical length of plant[m]
        'k' : 0.001, #rate of plant growth
        "NpX" : int(48), #plants in X-direction
        "NpY" : int(48), #plants in Y-direction
        'Nsteps': int(days/dt),
        'dt': 0.1,
            }        

#allocate position and initial vars
X = np.zeros((farm['NpX'],farm['NpY']))
Y = np.zeros((farm['NpX'],farm['NpY']))
lsl = np.zeros((farm['NpX'],farm['NpY']),dtype=bool) #flag variable for infected plants
S = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
L = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
I = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
R = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
P = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
E = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))

#assign intial conditions 
for i in range(farm['NpX']):
    for j in range(farm['NpY']):
        X[i,j] = i * farm['LpX'] - 0.5 #x-position of center of a plant [m]
        Y[i,j] = j * farm['LpY'] - 0.5 #y-position of center of a plant [m]
        S[i,j,0]=1
        L[i,j,0]=0
        I[i,j,0]=0
        R[i,j,0]= farm['mu_I'] * L[i,j,0]
        P[i,j,0]=1
        E[i,j,0]=0

#pathogen growth
#insert the pathogen and select 1 plant in the middle of the field that is infectious
I[int(farm['NpX']/2),int(farm['NpY']/2),0]= 1
L[int(farm['NpX']/2),int(farm['NpY']/2),0]= 0.001*S[i,j,0]

initial_population = S.sum() + L.sum() + I.sum() + R.sum() + P.sum() + E.sum()

#call pathogen growth function
start_time = time.time()
[S,L,I,R,P,E] = pathogen_growth_2D(S,L,I,R,P,E,lsl,T,T_min,T_max,U,V,tspan, farm)
stop_time = time.time()
print(f'Simulated in {stop_time - start_time} seconds')
# # Normalize each compartment by the initial population size
# S /= initial_population
# L /= initial_population
# I /= initial_population
# R /= initial_population
# P /= initial_population
# E /= initial_population

# Update the populations list with normalized values
populations = [S, L, I, R, P, E]



#Plotting figure 3:
plt.figure()
plt.xlabel("time [days]")
plt.ylabel("Population [fraction of initial]")
plt.plot(tspan, populations[0][int(farm['NpX']/2),int(farm['NpY']/2),:], label='S',color ='m',linestyle='dashdot')
plt.plot(tspan, populations[1][int(farm['NpX']/2),int(farm['NpY']/2),:], label='L',color ='g', linestyle='dashed')
plt.plot(tspan, populations[2][int(farm['NpX']/2),int(farm['NpY']/2),:], label='I',color='b', linestyle='dotted')
plt.plot(tspan, populations[3][int(farm['NpX']/2),int(farm['NpY']/2),:], label='R',color ='r', linestyle='dashdot')
plt.plot(tspan, populations[4][int(farm['NpX']/2),int(farm['NpY']/2),:], label='P',color ='k')
#plt.plot(tspan, populations[5][int(farm['NpX']/2),int(farm['NpY']/2),:], label='E')
#plt.legend()

plt.show()

#Plot figure 4:
# Extract the final time step data for each variable
time_index = -1  # Last timestep for final state at 75 days
final_S = S[:, :, time_index]
final_L = L[:, :, time_index]
final_I = I[:, :, time_index]
final_R = R[:, :, time_index]
final_P = P[:, :, time_index]
final_E = E[:, :, time_index]

# Calculate averages over the domain
avg_S = final_S.mean()
avg_L = final_L.mean()
avg_I = final_I.mean()
avg_R = final_R.mean()
avg_P = final_P.mean()
avg_E = final_E.mean()

# Titles for each subplot with average values
titles = [
    f'<P> = {avg_P:.5f}', f'<S> = {avg_S:.5f}', f'<L> = {avg_L:.5f}',
    f'<I> = {avg_I:.5f}', f'<R> = {avg_R:.5f}', f'<E> = {avg_E:.5f}'
]

# Prepare data for plotting
variables = [final_P, final_S, final_L, final_I, final_R, final_E]
x = np.linspace(0, 48, 48)  # x-axis in meters
y = np.linspace(0, 48, 48)  # y-axis in meters
X, Y = np.meshgrid(x, y)

# Plot setup
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('2D SLIRPE Model of Pathogen Spread (75 days)', fontsize=16)

for i, (ax, data, title) in enumerate(zip(axs.flatten(), variables, titles)):
    contour = ax.contourf(X, Y, data, cmap='viridis')  # Use 'viridis' for color scheme
    fig.colorbar(contour, ax=ax, orientation="vertical")
    ax.set_title(title, fontsize=12)
    ax.set_xlabel('X (meters)')
    ax.set_ylabel('Y (meters)')

# Adjust layout 
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

#Calculate averages (for titles)
total_elements = farm['NpX'] * farm['NpY']
avg_S = S.sum() / total_elements
avg_L = L.sum() / total_elements
avg_I = I.sum() / total_elements
avg_R = R.sum() / total_elements
avg_P = P.sum() / total_elements
avg_E = E.sum() / total_elements
averages = [f'<S> = {avg_S:.6f}', f'<L> = {avg_L:.6f}', f'<I> = {avg_I:.6f}', 
            f'<R> = {avg_R:.6f}', f'<P> = {avg_P:.6f}', f'<E> = {avg_E:.6f}']


#plot infection spread
time_index_at_plot = -1
titles =['Susceptible', 'Latent', 'Infectious', 'Remissive', 'Population', 'External']

fig, axs = plt.subplots(2, 3, figsize=(12, 8))
fig.suptitle(f'Populations of interest at t = {tspan[time_index_at_plot]} days')

x = np.arange(farm['NpX'])
y = np.arange(farm['NpY'])
X, Y = np.meshgrid(x, y)

for index, population in enumerate(populations):
    ax = axs[index // 3, index % 3]
    contour = ax.contourf(X, Y, population[:, :, time_index_at_plot], cmap='viridis', label=' ')
    fig.colorbar(contour, ax=ax)
    ax.set_title(titles[index] + " " + averages[index])

# Adjust subplots
plt.subplots_adjust(hspace=0.5)
axs[0, 0].legend(loc='upper right')
plt.show()
    