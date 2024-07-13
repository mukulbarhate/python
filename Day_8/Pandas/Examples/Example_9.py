# DataFrame is a two dimensional labelled data structure
# DataFrame comprises of rows and columns

from pandas import *

mydict={"Name":['Sachin','Rahul','Anil'],"Age":[30,35,38]}
print(mydict)
mydataframe=DataFrame(mydict)
print(mydataframe)
print("\n")
print(type(mydataframe))

