# How to create series object from dictionary
from pandas import *

mydict=({1:'Sachin',2:'Rahul',3:'Anil',4:'Rohit'})
print(mydict)
print("\n")
print(type(mydict))
print("Let's create Series from a dictionary")
myseries=Series(mydict)
print(myseries)
print(myseries.index)
print(myseries.values)