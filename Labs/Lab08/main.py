from eulerSolve import euler
import system_ODE
import matplotlib.pyplot as plt
import numpy as np


initial_conds = [1 , 0.001, 0, 0, 1] #SLIRP, S = P (all of population is susceptible, no infections)
#beta, muL, muI, e, k, Tmin, Tmax, T
pop_params = [2, 2, 4, 0.005, 0.001, 10, 35, 25]

def plot_population(init_conds, time_params, pop_params, ax, title):
    values, t_range = euler(system_ODE.system_ODE, initial_conds, [0, 30, 0.1], pop_params)
    ax.set_title(title)
    ax.plot(t_range, values[0, :], label='Susceptible')
    ax.plot(t_range, values[1, :], label='Latent')
    ax.plot(t_range, values[2, :], label='Infected')
    ax.plot(t_range, values[3, :], label='Removed')
    ax.plot(t_range, values[4, :], label='Population')
    ax.set_xlabel('Time [days]')
    ax.set_ylabel('Population')
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=8)

titles = ['beta', 'muL', 'muI', 'e']

values = [ 
    [.75, 2, 3],        #beta
    [.75, 2, 4],        #muL
    [.75, 2, 40],        #muI
    [1e-5, 5e-3, .04]   #e
    
]

for i in range(4):
    fig, axs = plt.subplots(3, 1, figsize=(12, 8))
    fig.suptitle(f'Variation of {titles[i]}')
    for n in range( 3):
        pp_local = np.copy(pop_params)
        pp_local[i] = values[i][n]
        plot_population(initial_conds, [0, 30, 0.1], pp_local, axs[n], f'{titles[i]} = {pp_local[i]}')
    
    plt.subplots_adjust(hspace=0.5)
    axs[0].legend(loc='upper right')
    plt.show()


# Parameter: Beta
# Beta changes how fast the epidemic spreads, so a higher beta value will correlate with a faster
# growth rate for the infected population. 

# Parameter: muL
# muL determines how long before the latent population becomes infected. This means that for an increase
# in muL, there will be a larger and larger latent population. A higher muL value also slows down how fast
# an infection spreads.

# Parameter: muI
# muI determines the length of time for an infected population moves to the removed/recoved stage. Incresing
# muI decreases the proportion of the population that becomes infected. 

# Parameter: e
# e controls infections from external sources. increasing the value of e will make the epidemic progress faster.
# Similarly, a smaller e value will lead to a slower development of the epidemic.

# Conclusion:
# I would target decreasing muI to limit the spread of the disease. This variable was the only variable that significantly
# reduced the peak of the infected population. 