# Example 2D array
import numpy as np

data = [
    [7, 3, 9, 4],
    [6, 2, 10, 1],
    [4, 8, 5, 7],
    [9, 3, 2, 8],
    [5, 6, 7, 9]
]

data2 = [
    [7, 3, 9, 4],
    [6, 2, 10, 1],
    [4, 8, 5, 7],
    [9, 3, 2, 8],
    [5, 6, 7, 9]
]
vector1 = np.array(data)
vector2 = np.array(data2)
data = vector1 + vector2

# Iterating through the 2D array using nested for loops
for i in range(len(data)):         # Outer loop for rows
    for j in range(len(data[i])):  # Inner loop for columns
        print(f"Value at row {i}, column {j}: {data[i][j]}")

