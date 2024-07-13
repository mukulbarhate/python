from pandas import *

mylist=[]
print("enter 10 values")
for i in range(1,11):
    num=int(input())
    mylist.append(num)
myseries=Series(mylist)

print(myseries)
print("\n")
print(myseries[3])              #  extract 3rd element
print("\n")
print(myseries[4:7])            #  extract 4th to 6th elements
print("\n")
print(myseries[-4:])            #  4th last till end
print("\n")
print(myseries[:3])             #  extract first 3 elements
print("\n")
print(myseries[5:])             #  extract from 5th position