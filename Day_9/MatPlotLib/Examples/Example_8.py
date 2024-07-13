"""  Box Plot displays the five-number summary of a set of data. 
The five-number summary is the minimum, first quartile, median, third quartile, and maximum.  """

""" The first quartile (Q1), is defined as the middle number between the smallest number and the median of the data set, the second quartile (Q2) – median of the given data set while the third quartile (Q3), is the middle number between the median and the largest value of the data set.
 """

from matplotlib import pyplot as py
import statistics
first=[1,2,3,4,5,6,7,8,9]
second=[1,2,3,4,5,4,3,2,1]
third=[6,7,8,9,8,7,6,5,4]

print("Median of first is\t",statistics.median(first))
print("Median of second is\t",statistics.median(second))
print("Median of third is\t",statistics.median(third))

data=list([first,second,third])
py.boxplot(data,labels=['first','second','third'])
py.show()