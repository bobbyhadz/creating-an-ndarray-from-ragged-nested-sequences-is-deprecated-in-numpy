# Creating ndarray from ragged nested sequences is deprecated

import numpy as np

def get_arr():
    arr = np.array([[1], [1, 2], [1, 2, 3]], dtype=object)
    return arr


result = get_arr()

# 👇️ [list([1]) list([1, 2]) list([1, 2, 3])]
print(result)