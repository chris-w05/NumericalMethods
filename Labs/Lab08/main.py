from eulerSolve import euler
import system_ODE
import matplotlib.pyplot as plt


initial_conds = [ 1, 1, 0.001, 0, 0] #PSLIR, S = P (all of population is susceptible, no infections)
values, t_range = euler(system_ODE.system_ODE, initial_conds,[0, 30, .1] )


plt.figure()
plt.plot(t_range, values[0,:], label='Susceptible')
plt.plot(t_range, values[1,:], label='Latent')
plt.plot(t_range, values[2,:], label='Infected')
plt.plot(t_range, values[3,:], label='Removed')
plt.plot(t_range, values[4,:], label='Population')
plt.legend()
plt.xlabel('Time [days]')
plt.ylabel('Population')
plt.show()


