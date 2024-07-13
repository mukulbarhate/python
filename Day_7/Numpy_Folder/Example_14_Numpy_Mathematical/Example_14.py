# axis-0 for column-wise sum
# axis-1 for row-wise sum

import numpy as np

first=np.array([10,20,30])
second=np.array([40,50,60])
third=np.sum((first,second),axis=0)     # column_wise
# [50 70 90]
print(third)
print("\n\n")
fourth=np.sum((first,second),axis=1)    # row_wise
# [ 60 150]
print(fourth)

