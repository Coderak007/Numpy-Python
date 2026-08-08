# fancy indexing --- accessing elements using an array of indices

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

indices = np.array([0, 2, 4])  # Indices of elements
print(arr[indices])  # Output: [10 30 50] --- accessing elements at specified indices