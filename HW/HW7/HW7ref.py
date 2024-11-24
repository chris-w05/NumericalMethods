import numpy as np
E = 10*10**9        #Pa
I = 1.25*10**-5     #m^4
L = 3               #m

def power_method(A, num_iterations):
    n, m = A.shape
    x = np.ones(m)
    for _ in range(num_iterations):
        x = np.dot(A, x)
        x = x / np.linalg.norm(x)
    eigenvalue = np.dot(x, np.dot(A, x)) / np.dot(x, x)
    return eigenvalue

def finite_difference_matrix(n):
    h = 1 / (n - 1)
    A = np.zeros((n, n))
    for i in range(1, n-1):
        A[i, i-1] = 1
        A[i, i] = -2
        A[i, i+1] = 1
    A[0, 0] = A[-1, -1] = 1
    return A / (h**2)

def power_method(A, num_iterations):
    n, m = A.shape
    x = np.ones(m)
    for _ in range(num_iterations):
        x = np.dot(A, x)
        x = x / np.linalg.norm(x)
    eigenvalue = np.dot(x, np.dot(A, x)) / np.dot(x, x)
    return eigenvalue


# Example usage:
A = finite_difference_matrix(3)
num_iterations = 10
smallest_eigenvalue = power_method(A, num_iterations)
print("Smallest Eigenvalue:", smallest_eigenvalue)


n = 5
A = finite_difference_matrix(n)
for i in range(1, 6):
    eigenvalue = power_method(A, i)
    h_squared = (L/n)**2
    buckling_load = np.sqrt(np.abs(eigenvalue/h_squared))
    print(f"Iteration {i}: Buckling Load = {buckling_load}")
    


n = 10  # Increase the number of nodes
num_iterations = 100  # Increase the number of iterations
A = finite_difference_matrix(n)
eigenvalue = power_method(A, num_iterations)
h_squared = (L/n)**2
buckling_load = np.sqrt(np.abs(eigenvalue/h_squared))
print(f"Buckling Load = {buckling_load}")