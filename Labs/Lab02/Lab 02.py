#Lab 02 code
import numpy as np

A = [1, 2, 3, 4, 5]
B = [2, 3, 4, 5, 6]

C = [
    [1, 2, 3],
    [4, 5, 6],
]

D = [
    [1, 3, 5],
    [2, 4, 6],
]

E = [
    [1, 2],
    [4, 5],
    [5, 6]
]

#find 5 * A - 2
output = np.subtract( np.multiply(A, 5), 2)
print("5 * A - 2 = " , output)

#subtract 5 * first row from second row of D
output = np.zeros_like(D)
output[0][:] = D[0][:]
for i in range(0, len(D[0])):
    output[1][i] -= D[0][i] * 5
print("subtract 5 * first row from second row of D = " , output) 


#Calculate A + B
#using for loop
output = np.zeros_like(A)
for i in range(0, len(A)):
    output[i] = A[i] + B[i]
print("A + B (manual)= " , output)

#using built in functions
output = np.add(A, B)
print("A + B = " , output)


#Calculate C + D
output = np.zeros_like(C)
for i in range(0, len(C)):
    for j in range(0, len(C[i])):
        output[i][j] = C[i][j] * D[i][j]
print("C + D (manual) = " , output)        
#using built in funciton
output = np.multiply(C, D)
print("C + D = " , output)


#Sums
#Sum of all elements in A
sum = 0
for item in A:
    sum += item
print("Sum of elements in A (manual) = " , sum)

sum = np.sum(A)
print("Sum of elements in A = " , sum)


#Sum of all elements in C
sum = 0
for i in C:
    for j in i:
        sum += j
print("Sum of elements in C (manual) = " , sum)

sum = np.sum(C)
print("Sum of elements in C = " , sum)

sum = np.sum(C[1])
print("Sum of elements in second row of C = " , sum)


#Dot product
#A dot B
sum = 0
for i in range( 0, len(A)):
    sum += A[i] * B[i]
print("A dot B = %d" % sum)

sum = np.dot( A, B)
print("A dot B = %d" % sum)

#takes a colunm and converts it to a row
def column( matrix, i ):
    return [row[i] for row in matrix]

sum = np.dot( D[0] , column(E, 0))
print("First row of D dot first column of E = %d" % sum)


def matrix_mult(X, Y):
    output = np.zeros((len(X), len(Y[0])))
    #Check if arrays are the same size
    if len(X) != len(Y[0]):
        raise ValueError('Matrices not of same size')
    #go through every spot in output array, and take dot product of 'overlapping' vectors
    for i in range(len(X)):
        for j in range(len(Y[i])):
            value = np.dot(X[i], column(Y, j))
            output[i][j] = value
    return output

output = matrix_mult(D, E)
print("D * E (matrix_mult)= " , output)

output = np.matmul(D, E)
print("D * E = " , output)

#Fibonnaci series
def fibonacci(N):
    output = [0,1]
    while len(output) < N:
        #New term is sum of previous two terms
        output.append(output[-1] + output[-2])
    return output

n = 10
output = fibonacci(n)
print("Fibonnaci to %d terms = " % n, output)