# Boolean masking --- filtering elements based on a condition

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
condition = arr > 25  # Boolean condition
print(arr[condition])  # Output: [30 40 50] --- filtering elements greater than 25