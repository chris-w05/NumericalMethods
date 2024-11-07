import Linsolve
import numpy as np
#Problem 1:
A = [[-1.56, .08, 0],
     [.48, -1.56, .08],
     [0, .48, -1.56]]

b = [-5 - 5*(.48), -10, -15 - 8*(.08)]

x = Linsolve.naive_gauss_elimination(A, b)
solution = [5.0]
solution.extend(x)
solution.append(8.0)
print(f'values for x = 0:20 in increments of 5: {solution}')



#Problem 3:

#Constants:
h0 = 20      #W/mK
k = 200     #W/mK
L = 2       #m
D = 0.1     #m
Tinf = 300  #K
Tb = 600    #K
Te = 350    #K

P = D*np.pi
A = np.pi * (D/2)**2
c = h0*P/(k*A)    

h = .5
alpha = 1/h**2
beta = -2/h**2 - 4 #hP/kA = 4
gamma = 1/h**2
hpkaT = -1200 #
A = [[beta, gamma, 0],
     [alpha, beta, gamma],
     [ 0, alpha, beta]]
b = [ hpkaT - 600*alpha, hpkaT, hpkaT - 350*gamma]
solution = [600]
solution.extend( Linsolve.naive_gauss_elimination(A, b))
solution.append(350)
print(solution)