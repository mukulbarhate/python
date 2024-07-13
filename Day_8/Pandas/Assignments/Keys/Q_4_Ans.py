from pandas import *

mylist=[]
print("Enter 5 values")
for i in range(1,6):
    num=int(input())
    mylist.append(num)

myseries=Series(mylist)
print(myseries)
print("\n")
print(myseries.sum())
print("\n")
print("Enter value to be added in the series")
val=int(input())
print(myseries.add(val))
print("enter value to be subtracted from the series")
val=int(input())
print(myseries.sub(val))
print("enter value to be multiplied by the series")
val=int(input())
print(myseries.mul(val))
print("enter value to be devided by the series")
val=int(input())
print(myseries.div(val))