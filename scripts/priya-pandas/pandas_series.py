import pandas as pd

import numpy as np


array1=np.array([1,2,3,4,])
#same data type

series1 = pd.Series(array1)

print(series1)

array2=np.array([['add','subtract','multiply','divide'],[23,24],[10,12]])

print(array2)

series2 = pd.Series(array2)

print(series2)

array3=np.array([12,34,56])

print(array3)

series3 = pd.Series(array3)

print(series3)

"""

array4=np.array([12,34,56])

print(array4)

series4=pd.Series(array4)
"""