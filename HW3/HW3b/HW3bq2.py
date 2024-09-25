import numpy as np

array = np.array([[5, 1, -.5, 13.5],
                  [-6, -12, 4, -123],
                  [-2, 2, 10, -43]])

def reduce(array, printSteps=False):
    rows = len(array)
    cols = len(array[0])
    
    U = np.array(array, dtype=float)  # Copy of array for U (upper triangular)
    L = np.array(rows)  # Identity matrix for L (lower triangular)
    
    print(L)
    # Create upper triangle (U matrix)
    for k in range(0, rows):
        if printSteps:   
            print(f"Pivot row (U): {k}")
        for i in range(k+1, rows):
            s = U[i][k] / U[k][k]
            for j in range(k, cols):
                U[i][j] = U[i][j] - s * U[k][j]
            if printSteps:   
                print("Step in U matrix:")
                print(U)
                print()
    
    
    #Create lower triangle
    for k in range(0, rows):
        if printSteps:   
            print(f"Pivot row (U): {k}")
        for i in range(0, k):
            s = L[i][k] / L[k][k]
            for j in range(k, cols):
                L[i][j] -= s * L[k][j]
            if printSteps:   
                print("Step in U matrix:")
                print(L)
                print()
                
    # Normalize L by dividing each element by the pivot
    for m in range(0, rows):
        leadingValue = L[m][m]
        if leadingValue != 0:  # Avoid division by zero
            for n in range(0, m+1):
                L[m][n] /= leadingValue
        if printSteps:   
            print(L)
            print()
    
    return L, U

L, U = reduce(array, printSteps=False)