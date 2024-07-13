# violinplot

"""

In a violin plot, quantiles represent the statistical distribution of the data.
Quantiles are points that divide a dataset into equal-sized continuous subsets.
In a violin plot, the quantiles are typically displayed as horizontal lines
within the "violin" shape, providing insights into the distribution's
characteristics such as the median, quartiles, or any other specified quantiles.

"""
import statistics
from matplotlib import pyplot as py

first=[1,2,3,4,5,6,7,8,9]
second=[1,2,3,4,5,4,3,2,1]
third=[6,7,8,9,8,7,6,5,4]

data=list([first,second,third])
# try quantiles=[[0.25,0.5],[0.25,0.5,0.75],[0.25,0.5,0.75]
# try quantiles=[[0.5],[0.25,0.5,0.75],[0.25,0.5,0.75]
    # and so on....
py.violinplot(data,showmedians=True,quantiles=[[0.25,0.5,0.75],[0.25,0.5,0.75],[0.25,0.5,0.75]])
#py.violinplot(data)
#print(py.violinplot.__doc__)
print(statistics.mean(first))
print(statistics.mean(second))
print(statistics.mean(third))
py.show()