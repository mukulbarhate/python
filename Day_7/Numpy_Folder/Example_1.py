# create single dimensional array

import numpy as np         # type: ignore #  here "numpy" is a module and "np" is an alias

first=np.array([[100,200,300,400],[10,50,5,55]])
print(first)

for i in range(0,first.__len__()):
    print(first[i])

print(type(first))
print("dimension of array is\t",first.ndim)         # This is for Dimension of Array
print("\n")
print("shape of array is\t",first.shape)            # This will give you Shape of Array

# first[4]=500     #  arrays are fixed

