import numpy as np

array = np.array([[5, 1, -.5, 13.5],
                  [-6, -12, 4, -123],
                  [-2, 2, 10, -43]])


def reduce(array, printSteps=False):
    rows = len(array)
    cols = len(array[0])
    if array[0][0] == 0:
        index = 1
        while array[index][0] == 0:
            index += 1
            if index > len(array):
                raise KeyError
        temp = array[0]
        array[index] = array[0]
        array[0] = temp
    
      
    if printSteps:   
        print(array)
        print("\nConverting to upper triangular")

    #Convert to RREF
    for k in range(0, rows):
        if printSteps:   
            print(f"Pivot row: {k}")
        for i in range(k+1, rows):
            s = array[i][k] / array[k][k]
            for j in range(k, cols):
                array[i][j] = array[i][j] - s * array[k][j]
            if printSteps:   
                print(array)
                print()
    
    if printSteps:   
        print("\nScaling rows")
    
    #Make leading values equal to one
    for m in range(0, rows):
        leadingValue = array[m][m]
        for n in range( m, cols):
            array[m][n] /= leadingValue
        if printSteps:   
                print(array)
                print()
    
    if printSteps:   
        print("\nEliminating rows")

    #Eliminate other rows
    for k in range(1, rows):
        #All rows other than m
        if printSteps:   
            print(f"Pivot row: {k}")
        for m in list(range(0,k)) + list(range(k+1,rows)):
            s = array[m][k]/array[k][k]
            for n in range(k,cols):
                array[m][n] -= s*array[k][n]
            if printSteps:   
                print(array)
                print()
    return array


print(reduce(array))