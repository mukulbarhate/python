from numpy import *
first=array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(first)
print("\n")
print(first[1:2,])     #  display   50  60  70  80
print("\n")
print(first[2,1:3])    # display 100 and 110
print("\n")
print(first[0:3,2:3])  # display 30 70 and 110
print("\n")
print(first[1:3,0:2])  # display 50  60  90 and 100
