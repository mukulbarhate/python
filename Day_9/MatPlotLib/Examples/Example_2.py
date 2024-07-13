from turtle import color
from numpy import *
from matplotlib import pyplot as py

x=arange(1,10)
print(x)
print("Type of x is\t",type(x))
y=x*2
print(y)
print("Type of y is\t",type(y))

py.plot(x,y,color='g',linestyle='dotted',linewidth=2)
py.title("Data Visualisation")
py.xlabel("x axis data")
py.ylabel("y axis data")
py.grid(True)
py.show()