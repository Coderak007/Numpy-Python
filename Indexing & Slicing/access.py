"""
array[index] - Accessing a single element in the array using its index.
array[start:stop] - Slicing the array to access a range of elements from start index
    to stop index (exclusive).
array[start:stop:step] - Slicing the array with a step value to access elements at regular intervals.
array[condition] - Accessing elements that satisfy a specific condition (boolean indexing). 
array[row_index, column_index] - Accessing elements in a 2D array using row and column indices.

"""
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Output: 10 --- Accessing the first element
print(arr[1:4])  # Output: [20 30 40] --- Slicing from index 1 to 3 (4 is exclusive)
print(arr[::2])  # Output: [10 30 50] --- Slicing with a step of 2, accessing every second element
print(arr[::-1])  # Output: [50 40 30 20 10] --- Slicing with a negative step, reversing the array