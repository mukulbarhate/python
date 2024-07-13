# adding a scalar value to series elements  and adding two series
# Series is immutable but their elements can be changed

from pandas import *
myseries=Series([10,20,30,40,50])
print(myseries)
print("\n")
print(myseries+4)
print("\n")
myseries1=Series([1,2,3,4,5])
print(myseries+myseries1)




