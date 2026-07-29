import numpy as np

arr = np.array([1.4, 2.6, 3.5, 4.1, 5.9])
print(arr.dtype)  # Output: float64 --- data type of the array elements
int_arr = arr.astype(int)  # Convert float array to int array

print(int_arr)  # Output: [1 2 3 4 5]
print(int_arr.dtype)  # Output: int32 --- data type of the new array
