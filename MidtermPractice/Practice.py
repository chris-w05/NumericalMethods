import numpy as np
import matplotlib.pyplot as plt

b = np.zeros(3)
for i in range(3):
    if i == 0:
        b[i] = 0
    else:
        b[i] = 2*i + 1
print(b)
        
A = np.zeros((3,3))
for i in range(0,3):
    for j in range(0,3):
        A[i][j] = i + j
print(A)

c = np.zeros(3)
for i in range(0,3):
    sum = 0
    for j in range(0,3):
        sum += A[i][j] * b[j]
    c[i] = sum

print(c)

c = np.zeros(3)
for i in range(0,3):
    c[i] = np.sum( A[i][:] * b[:])
    
print(c)
        
#root finding:
e = 1.43e-6
rho = 1.38
mu = 1.91e-5
D = 0.0061
V = 54

x = np.linspace(0.0001, 2, 1000)

def g(f, e=e, rho=rho, mu=mu, D=D, V=V):
    Re = rho*V*D/mu
    out = (1/np.sqrt(f)) + 2*np.log(e/(3.7 * D) + 2.51/(Re*np.sqrt(f)))
    return out

y = np.zeros_like(x)
for i in range(0, len(x)):
    y[i] = g(x[i])


x = np.linspace(0.0001,1, 1000)

def g(f, e=e, rho=rho, mu=mu, D=D, V=V):
    Re = rho * V * D / mu
    out = (1 / np.sqrt(f)) + 2 * np.log10(e / (3.7 * D) + 2.51 / (Re * np.sqrt(f)))
    return out

y = np.zeros_like(x)
for i in range(len(x)):
    y[i] = g(x[i])

# Root-finding method: Bisection
roots = []

def bisection(a, b, tol=0.001):
    if g(a) * g(b) > 0:
        print("No root in the interval")
        return None
    prev = 0
    aError = 1
    while np.abs(aError) > tol:
        c = (a + b) / 2
        aError = np.abs((c - prev) / c)  # Fix absolute error calculation
        y = g(c)
        if y < 0:
            b = c
        else:
            a = c
        prev = c
        roots.append(c)
    
    return (a + b) / 2

# Plotting
# plt.figure()
# plt.plot(x, y, label="g(f)")
# plt.axhline(0, color='gray', linewidth=0.5)  # Add a horizontal line at y=0

# Execute bisection and plot root
guess = bisection(0.00001, 1)
if guess is not None:
    z = np.zeros(len(roots))  # Define z after finding the root
    plt.plot(roots, z, marker='*', linestyle='None', color='red', label="Roots")

# plt.legend()
# plt.show()

print("Root guess:", guess)
print(g(guess))

# Linear system:

def gauss( A, b):
    m,n = np.shape(A)
    x = np.zeros(n)
    for k in range(0,n):
        for i in range(k + 1, n):
            s = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - s*A[k][j]
            b[i] = b[i] - s*b[k]
    x[-1] = b[-1]/A[-1][-1]
    for i in range (n-2 , -1, -1):
        s = 0
        for j in range(i+1, n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

A = [[ .52, .2, .25 ],
     [.30, .5, .2],
     [.18, .3, .55]]
b = [2180, 5810, 5690]

x = gauss(A, b)
print(x)

print(np.linalg.solve(A, b))