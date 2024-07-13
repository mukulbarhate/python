from pandas import *

marks=[]
subjects=[]

print("enter subject and then marks respectively for 5 times")
for i in range(1,6):
    mysub=input()
    mynum=int(input())
    subjects.append(mysub)
    marks.append(mynum)

myseries=Series(marks,index=subjects)

print(myseries)