from numpy import *
from matplotlib import pyplot as py

first=arange(1,11)     #  x-axis
second=2*first         #  y-axis

print(first)
print("\n")
print(second)
py.plot(first,second)     #  line plot  just displays lists
#  here "first"  is  x-axis
#  "second" is y-axis
py.show()       # displays the graph
