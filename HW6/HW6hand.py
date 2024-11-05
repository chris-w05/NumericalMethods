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
h = .5
alpha = 1/h**2
beta = -2/h**2 - 4 #hP/kA = 4
gamma = 1/h**2
hpkaT = -2400
A = [[beta, gamma, 0],
     [alpha, beta, gamma],
     [0, alpha, beta]]
b = [hpkaT - alpha*600 , hpkaT, hpkaT - gamma*350]
x = Linsolve.naive_gauss_elimination(A, b)
solution = [float(600)]
solution.extend(x)
solution.append(float(350.0))
print(solution)
