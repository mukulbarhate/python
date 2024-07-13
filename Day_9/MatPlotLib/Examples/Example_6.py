# scatter plots

from numpy import *
from matplotlib import pyplot as py

first=arange(1,11)
second=2*first

py.scatter(first,second,marker="*",c='r',s=200)     #  scatter plot  ,   first and second must have same no. of elements 
py.show()