# extracting elements from the series

from pandas import *

myseries=Series([10,20,30,40,50,60,70,80])
print(myseries)
print("\n")
print(myseries[5])              # extract 5th element
print("\n")
print(myseries[2:6])            # extract elements from 2 to 5
print("\n")
print(myseries[-6:-3])          # extract elements from sixth last to fourth last
print("\n")
print(myseries[:4])             # extract first 4 elements
print("\n")
print(myseries[3:])             # extract elements from the 3rd position

