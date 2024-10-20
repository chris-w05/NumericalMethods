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

#Redoing matric problems
#Just in case:
x = [0, 1, 2, 3, 4]
y = [1, 4, 2, 7, 1]

deg = len(x)
constants = np.polyfit(x, y, deg )    
func = np.poly1d(constants)

vec = np.zeros(deg)
for i in range(0,deg):
    vec[i] = func(i)
b =vec
print(vec)

rows, cols = 5,5
vec = np.zeros( (rows,cols))
for i in range(0, rows):
    for j in range(0, cols):
        vec[i][j] = i*cols + j
A = vec
print(vec)

#dot product:
c = np.zeros_like(b)
for i in range(0,len(A)):
    c[i] = np.sum( A[i][:] * b[:])
print(c)
print(np.matmul(A, b))


    
        
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


# # Plotting
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


#Fixed point method:
def nextVal(guess):
    Re = rho * V * D / mu
    return (1/(-2.0*np.log((e/3.7*D) + 2.51/(Re*np.sqrt(guess)))))**2

def fixedPoint( guess, function, tol=1e-6):
    error = 1
    while error > tol:
        previousGuess = guess
        guess = function(guess)
        error = (guess - previousGuess)/guess
    return guess

root = fixedPoint( 1, nextVal)
print(root)

#Secant method:
def secantMethod( a, b, function, tol=1e-6):
    error = 1
    while np.abs(error) > tol:
        print(f'A = {a}, B = {b}')
        ay = g(a)
        by = g(b)
        m = (by - ay)/(b - a)
        new_a = a - g(a)/m
        a,b = b, new_a
        error = (a-b)/a
        print(f'error = {error}')
    return a

#print(secantMethod( 0.001, .5 , g))
#Secant method is not suited to values near asymptotes


#False position method:
def falsePosition(a, b, function, tol=1e-6):
    error = 1
    fa = function(a)
    fb = function(b)
    
    if fa * fb > 0:
        print("No root in the interval")
        return None
    
    while np.abs(error) > tol:
        # False position formula
        c = (a * fb - b * fa) / (fb - fa)
        fc = function(c)
        
        if fa * fc < 0:  # Root is between a and c
            b = c
            fb = fc
        else:  # Root is between c and b
            a = c
            fa = fc
        
        # Update the error
        error = function(c)
    
    return c

print(f'False position: {falsePosition(.001, .1, g)}')




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