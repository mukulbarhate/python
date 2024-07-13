# changing index 

from pandas import *

myseries=Series([10,20,30,40,50])
print(myseries)
myseries.index=['a','b','c','d','e']
print(myseries)
print(myseries[0])
# print(myseries['d'])            # This is possible you can also use this to get the values
myseries[1]=65   # possible
# myseries['a']=45                # This is possible you can change the value of the elemeent
print(myseries)
