# -*- coding: utf-8 -*-
"""
EXTRA Code we may or may not want to use 
"""
#STUFF TO DO BEFORE A TRIAL 
# #allocate position and initial vars
# X = np.zeros((farm['NpX'],farm['NpY']))
# Y = np.zeros((farm['NpX'],farm['NpY']))
# lsl = np.zeros((farm['NpX'],farm['NpY']),dtype=bool) #flag variable for infected plants
# S = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
# L = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
# I = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
# R = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
# P = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))
# E = np.zeros((farm['NpX'],farm['NpY'],farm['Nsteps']))

# #assign intial conditions 
# for i in range(farm['NpX']):
#     for j in range(farm['NpY']):
#         X[i,j] = i * farm['LpX'] - 0.5 #x-position of center of a plant [m]
#         Y[i,j] = j * farm['LpY'] - 0.5 #y-position of center of a plant [m]
#         S[i,j,0]=1
#         L[i,j,0]=0
#         I[i,j,0]=0
#         R[i,j,0]= farm['mu_I'] * L[i,j,0]
#         P[i,j,0]=1
#         E[i,j,0]=0
###TO BE REPEATED AFTER CHANGING VARIABLES:
# #pathogen growth
# #insert the pathogen and select 1 plant in the middle of the field that is infectious
# I[int(farm['NpX']/2),int(farm['NpY']/2),0]= 1
# L[int(farm['NpX']/2),int(farm['NpY']/2),0]= 0.001*S[i,j,0]








# #Plotting figure 4:
# plt.figure()
# plt.xlabel("time [days]")
# plt.ylabel("Population [fraction of initial]")
# plt.title("Initial infection at X=11.5 Y=23.5")
# plt.grid(True)
# plt.plot(tspan, populations[4][int(farm['NpY']/2),int(farm['NpY']/2),:], label='Total Population',color ='k')
# plt.plot(tspan, populations[0][int(farm['NpY']/2),int(farm['NpY']/2),:], label='Susceptible',color ='m',linestyle='dashdot')
# plt.plot(tspan, populations[1][int(farm['NpY']/2),int(farm['NpY']/2),:], label='Latent',color ='g', linestyle='dashed')
# plt.plot(tspan, populations[2][int(farm['NpY']/2),int(farm['NpY']/2),:], label='Infected',color='b', linestyle='dotted')
# plt.plot(tspan, populations[3][int(farm['NpY']/2),int(farm['NpY']/2),:], label='Removed',color ='r', linestyle='dashdot')
# plt.plot(tspan, populations[5][int(farm['NpY']/2),int(farm['NpY']/2),:], label='External',color ='r', linestyle='dotted')
# plt.legend()
# plt.show()

# # Plotting the averages over time
# # Initialize lists to store the average values at each time step
# avg_S_list = []
# avg_L_list = []
# avg_I_list = []
# avg_R_list = []
# avg_P_list = []
# avg_E_list = []

# # Loop to update the populations and compute averages over the grid at each time step
# for t in range(farm['Nsteps']):
#     # Assuming S, L, I, R, P, E are updated by pathogen_growth_2D
#     avg_S_list.append(np.mean(S[:, :, t]))
#     avg_L_list.append(np.mean(L[:, :, t]))
#     avg_I_list.append(np.mean(I[:, :, t]))
#     avg_R_list.append(np.mean(R[:, :, t]))
#     avg_P_list.append(np.mean(P[:, :, t]))
#     avg_E_list.append(np.mean(E[:, :, t]))

# # Plotting the averages over time
# plt.figure(figsize=(10, 6))
# plt.plot(tspan, avg_P_list, label='Total Population',color ='k')
# plt.plot(tspan, avg_S_list, label='Susceptible',color ='m',linestyle='dashdot')
# plt.plot(tspan, avg_L_list, label='Latent',color ='g', linestyle='dashed')
# plt.plot(tspan, avg_I_list, label='Infected',color='b', linestyle='dotted')
# plt.plot(tspan, avg_R_list, label='Removed',color ='r', linestyle='dashdot')
# plt.plot(tspan, avg_E_list, label='External',color ='r', linestyle='dotted')

# plt.xlabel("Time [days]")
# plt.ylabel("Population [fraction of initial]")
# plt.title("Average Epidemic Response Over the Entire Field")
# plt.legend()
# plt.grid(True)
# plt.show()







# #Calculate averages (for titles)
# total_elements = farm['NpX'] * farm['NpY']
# avg_S = S.sum() / total_elements
# avg_L = L.sum() / total_elements
# avg_I = I.sum() / total_elements
# avg_R = R.sum() / total_elements
# avg_P = P.sum() / total_elements
# avg_E = E.sum() / total_elements
# averages = [f'<S> = {avg_S:.6f}', f'<L> = {avg_L:.6f}', f'<I> = {avg_I:.6f}', 
#             f'<R> = {avg_R:.6f}', f'<P> = {avg_P:.6f}', f'<E> = {avg_E:.6f}']


# #Calculate averages (for titles)
# total_elements = farm['NpX'] * farm['NpY']
# avg_S = S.sum() / total_elements
# avg_L = L.sum() / total_elements
# avg_I = I.sum() / total_elements
# avg_R = R.sum() / total_elements
# avg_P = P.sum() / total_elements
# avg_E = E.sum() / total_elements
# averages = [f'<S> = {avg_S:.6f}', f'<L> = {avg_L:.6f}', f'<I> = {avg_I:.6f}', 
#             f'<R> = {avg_R:.6f}', f'<P> = {avg_P:.6f}', f'<E> = {avg_E:.6f}']


# #plot infection spread
# time_index_at_plot = -1
# titles =['Susceptible', 'Latent', 'Infectious', 'Remissive', 'Population', 'External']

# fig, axs = plt.subplots(2, 3, figsize=(12, 8))
# fig.suptitle(f'Populations of interest at t = {tspan[time_index_at_plot]} days')

# x = np.arange(farm['NpX'])
# y = np.arange(farm['NpY'])
# X, Y = np.meshgrid(x, y)

# for index, population in enumerate(populations):
#     ax = axs[index // 3, index % 3]
#     contour = ax.contourf(X, Y, population[:, :, time_index_at_plot], cmap='viridis')
#     fig.colorbar(contour, ax=ax)
#     ax.set_title(titles[index] + " " + averages[index])

# # Adjust subplots
# plt.subplots_adjust(hspace=0.5)
# # axs[0, 0].legend(loc='upper right')
# plt.show()