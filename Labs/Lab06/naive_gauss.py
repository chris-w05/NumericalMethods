import numpy as np

def naive_gauss_elimination(a,b):
    #size checking:
    m,n = np.shape(a)
    if m != n:
        raise TypeError('A is not a square matrix')
    if len(a) != len(b):
        raise TypeError('A is not the same size as B')
    #Forward elimination
    for k in range(0, n-1):
        for i in range(k+1, n):
            s = a[i][k]/a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - s*a[k][j]
            b[i] = b[i] - s*b[k]
    
    #Backwards solve
    x = np.zeros(n)
    x[-1] = b[-1]/a[-1][-1]
    for i in range(n-2, -1, -1):
        s = 0
        for j in range( i +1, n):
            s = s + a[i][j]*x[j]
        x[i] = (b[i] - s)/a[i][i]
        
    return x