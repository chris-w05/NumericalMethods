import numpy as np

A = np.array([[6, -1, -1],
              [6, 9, 1],
              [-3, 1, 12]])
b = np.array([50, 3, 40])

solution = np.linalg.solve(A,b)
print(f'Solution using built in funciton: x ={solution}')

def solve(A, b, x, tol=1e-6, max_iter=10):
    n = len(b)
    iter = 0
    while iter < max_iter:
        previous_x = x.copy()  # Make a full copy of the current solution
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += A[i][j] * x[j]
            x[i] = (b[i] - sum) / A[i][i]  # Gauss-Seidel update
        if max(np.abs(np.subtract(previous_x, x))) < tol:
            #print("Convergence reached")
            return x
        iter += 1

    return x

initial_guess = np.array([1.0,1.0,1.0])
x = solve(A, b, initial_guess)
print(f'Solution using gauss-seidel: x = {x}')

'''If the equations are not reordered, the algorithm is not guaranteed to converge.
This emanates from updating of the x vector, where dividing a by a small diagonal value
A[i][i] will cause the x value to "blow up"
'''