# extract DataFrame rows as list

from pandas import *

mydataframe=DataFrame({"proid":range(1,5),"proname":['soap','perfume','deo','powder']})
print(mydataframe)
mylist=mydataframe.loc[[0]].values.tolist()
print(mylist)
print("\n")
mylist=mydataframe.loc[[0,1]].values.tolist()   # extract 0 and 1 rows
print(mylist)
mylist=mydataframe.loc[[1,3]].values.tolist()   # extract row no. 1 and 3 
print(mylist)
mylist=mydataframe.values.tolist()                # extract all rows
print(mylist)
mylist=mydataframe.iloc[:,0:1].values.tolist()    #  extract all rows of 0 to 1 columns, 1 is exclusive
print(mylist)
mylist=mydataframe.iloc[1:3,0:1].values.tolist()  # extract 1 to 3 rows and 0 to 1 columns, 3 and 1 are exclusive
print(mylist)