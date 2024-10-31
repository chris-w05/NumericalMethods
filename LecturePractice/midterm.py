import numpy as np
import matplotlib.pyplot as plt

b = np.zeros(4)
for i in range(0, len(b)):
    if i != 0:
        b[i] = (i + 1) * b[i - 1]
    else:
        b[i] = 1
print(b)


A = np.zeros((4, 3))
for i in range(np.shape(A)[0]):
    for j in range(np.shape(A)[1]):
        A[i][j] = (i + 1) * (j + 1)
print(A)

m, n = np.shape(A)
c = np.zeros(n)
for i in range(0, n):
    sum =0
    for j in range(0,m):
        sum += b[j] * A[j,i]
    c[i] = sum
print(f'The product is : {c}')

d = []


for i in range(0, n):
    sum = np.sum(b[:] * A[:,i])
    d.append(sum)
print(d)

# Newton-raphson method
def g(f, e=1.43e-6, rho=1.38, mu=1.91e-5, D=.0061, V=54):
    Re = rho*V*D/mu
    return (1/np.sqrt(f)) + 2 * np.log( (e/(3.7*D)) + 2.51/(Re * np.sqrt(f)))

def gPrime(f, e=1.43e-6, rho=1.38, mu=1.91e-5, D=.0061, V=54):
    Re = rho*V*D/mu
    return (-.5)*(f**(-3/2)) * (1.0 + (2.18261/Re) * (((e/D)/3.7) + (2.51/(Re*np.sqrt(f))))**-1 )


x = np.linspace(0.004, .01, 1000)
y = np.zeros_like(x)
for i in range(len(x)):
    y[i] = g(x[i])

plt.figure()
plt.plot(x, y)
plt.grid(True)
plt.xlabel('x axis')
plt.ylabel(' y axis')
plt.title('Newton-Raphson zero finding')


guess = .004


def newton(guess, func, funcDeriv, tol=.001):
    error = 1
    roots = []
    roots.append(guess)
    while np.abs(error) > tol:
        previousGuess = guess
        guess = guess - func(guess)/funcDeriv(guess)
        roots.append(guess)
        error = (guess - previousGuess)/guess
    return guess, roots

zero, roots = newton(guess, g, gPrime)
print(f'There is a zero at: {zero} in {len(roots)} iterations')
print('^If this is wrong, I probably entered the function g(f) or g\'(f) in wrong since my newton-raphson method worked for the last part')
zeros = np.zeros(len(roots))
plt.plot(roots, zeros, marker='*')
plt.show()


# Gauss elimination
def gauss(A, b):
    m, n = np.shape(A)
    x = np.zeros_like(b)
    for k in range(0, n-1):
        for i in range(k+1, n):
            s = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - s*A[k][j]
            b[i] = b[i] - s * b[k]

    x[-1] = b[-1]/A[-1][-1]
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i]-s)/A[i][i]
    return x


b = [750.5, 300, 102, 30]
A = [[13.442, 0, 0, 0],
     [-13.442, 12.252, 0, 0],
     [0, -12.252, 12.377, 0],
     [0, 0, -12.377, 11.797]]
A2 = [[13.442, 0, 0, 0],
     [-13.442, 12.252, 0, 0],
     [0, -12.252, 12.377, 0],
     [0, 0, -12.377, 11.797]]

x = gauss(A, b)
print(f'The c values are:{x}')
#print(np.matmul(A2, x))


#Function to find c4 in terms of change in b1
#X is the difference from b1
def concentration(x):
    b = [750.5, 300, 102, 30]
    A = [[13.442, 0, 0, 0],
         [-13.442, 12.252, 0, 0],
         [0, -12.252, 12.377, 0],
         [0, 0, -12.377, 11.797]]
    b[0] -= x
    c = gauss(A, b)
    return c[-1] - 75

def concentration_deriv(x):
    #Central difference method
    h = .1
    s1 = concentration(x + h)
    s2 = concentration(x - h)
    m = (s1 - s2)/(2*h)
    return m

c4, roots = newton(750, concentration, concentration_deriv)
print(f'The loading must be reduced by {c4} to achieve a chloride concentration of 75')


# print(newton(640, concen, concen_deriv))



