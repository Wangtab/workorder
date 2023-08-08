import numpy as np
import pandas as pd
# array结构
# 要求类型统一
array = np.array([[1, 2, 3, 4, 5], [2, 2, 3, 4, 5]])
array2 = np.array([[1.0, 2, 3, 4, 5], [2, 2, 3, 4, 5]])
print(array.shape, array + 1, array.dtype)
print(array2.shape, array2 + 1, array2.dtype)
