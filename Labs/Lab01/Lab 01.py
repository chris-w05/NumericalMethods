#Lab 01
import numpy as np

#Create an N x 1 (1D) array of integers that counts in sequence from 1 to N.
array1 = [x for x in range(1,10)]
print(array1)

#Create an N x M (2D) array of integers that counts in sequence from 1 to N*M, row-oriented.
N, M = 3, 3
array2 = [[ i + 1 for i in range(j*M,(j+1)*M)] for j in range(0,N)]
print(array2)

#Include the above code in a separate function that can be called. Inputs are: N, M, and a boolean option for row or column orientation.
def create_array(N: int,M=1 , row_orient=True):
    #Tried out doing a javadoc in python
    """Creates an array of dimesnions N,M and optionally orients

    Args:
        arg1 (int): Number of rows
        arg2 (in): Number of cols, default 1

    Returns:
        array: Array filled with 1 -> N*M either row or column oriented

    """
    output = []
    if M == 1:
        output = [x for x in range(1,10)]
    else:
        output = [[ i + 1 for i in range(j*M,(j+1)*M)] for j in range(0,N)]
    
    if not row_orient:
        return np.transpose(output)
    else:
        return output

#Utilize the create_array f unction to define and access data in a 1D array
array3 =  create_array(3)
print("First index value: %d\nLast index value %d" % (array3[0], array3[2]))

#Utilize the create_array f unction to define and access data in a 2D array 
# ❏ Input: N=3, M=3
# ❏ Outputs:
#   ❏ value at the first row, first column (i.e. 1)
#   ❏ value at the last row, last column (i.e. 9)
#   ❏ values from the entire first row (i.e. 1, 2, 3)
#   ❏ values from the entire last column (i.e. 3, 6, 9) 
#   ❏ values from the diagonal (i.e. 1, 5, 9)
N, M = 3, 3
array4 = create_array(N, M)
#First row, first col
print("Value at first row, first column: %d" % (array4[0][0]))

#Last row, last col
print("Value at the last row, last column: %d" % (array4[len(array4) - 1][len(array4[len(array4) - 1]) - 1]))

#Vals from first row
print("Values from the entire first row", end=" ")
print( array4[0])

#Vals from last column
columnArr = []
for i in range(0, len(array4)):
    columnArr.append(array4[i][2])
print("Values from the entire last column ", end=" ")
print(columnArr)

#values from diagonal
print("values from the diagonal: ", end=" ")
print( np.diag(array4))
