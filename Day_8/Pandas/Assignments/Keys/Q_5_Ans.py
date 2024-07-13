from pandas import *

mydict={}
names=[]
designations=[]
salaries=[]

print("Enter 5 names,designations and salaries")
for i in range(1,6):
    names.append(input())
    designations.append(input())
    salaries.append(int(input()))

mydict={"Names":names,"Designations":designations,"Salaries":salaries}

mydataframe=DataFrame(mydict)
print(mydataframe)

