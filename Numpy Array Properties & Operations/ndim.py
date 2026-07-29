import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr_1d.ndim)  # Output: 1 --- 1D array
print(arr_2d.ndim)  # Output: 2 --- 2D array  
print(arr_3d.ndim)  # Output: 3 --- 3D array