from numpy import *
first=full((3,3),'N')
for i in range(0,3):
    for j in range(0,3):
        print(first[i][j],end=" ")
    print("\n")