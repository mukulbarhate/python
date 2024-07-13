# extract DataFrame columns as list

from pandas import *

mydataframe=DataFrame({"proid":range(1,5),"proname":['soap','perfume','deo','powder']})
print(mydataframe)
mylist=mydataframe["proid"].values.tolist()       # extract values of "proid" only and convert them to list
print(mylist)
mylist2=mydataframe["proname"].values.tolist()       # extract values of "proname" only and convert them to list
print(mylist2) 
mylist=mydataframe[["proname","proid"]].values.tolist() # extract values of "proname and proid" and convert them to list
print(mylist)
mylist1=mydataframe[["proid","proname"]].values.tolist()
print(mylist1)                                    