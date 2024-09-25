import numpy as np
import matplotlib.pyplot as plt

A = np.array([[-2.2, 20],
             [-1, 8.7]])

detA = np.linalg.det(A)

print(f'The determinant is {detA}')

#Because the determinant is non-zero the system is not singular
x1 = np.linspace(402, 407, 100)

#Equations solved for x2, where the second digit is the equation the x2 value is taken from
x21 = (240 + 2.2*x1)/20
x22 = (87 + x1)/8.7

# Create the plot
plt.plot(x1, x21)
plt.plot(x1, x22)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.ylim((56.25, 56.75))
plt.title('Plot of 2x2 Matrix')

# Display the plot
plt.grid(True)
plt.show()

#There appears to be a solution at x1 = 404.5, x2 = 56.5