# DataFrame built-in functions
# copy "Book1.csv" file inside pycharm project folder

from pandas import *

book=read_csv("Book1.csv")
print(book)
print("type of book is\t",type(book))
print("\n")
print("Let's print first 5 records")
print(book.head())
print("\n")
print("let's print first 3 records")
print(book.head(3))
print("\n")
print("print all the records except last 3 records")
print(book.head(-3))   #  print all the records except last 3 records
print("Let's print last 5 records")
print(book.tail())  #  [-5:]
print("let's print last 2 records")
print("\n")
print(book.tail(2))  # [-2:]
print("\n")
print("print all the records except first 3 records")
#[-(-3):]
print(book.tail(-3))  #  print all the records except first 3 records
print("Total no. of rows and columns in the file")
print(book.shape)          # 10 rows and 3 columns
print("\n")
print(book.describe())     # it will give all the mathematical terms
print("\n")
print("Let's extract first 3 records with 2 columns only")
print(book.iloc[:3,:2])
print("\n")
print(book.loc[0:4,('name','address')])   #  Access a group of rows and columns by label(s) , 4 is inclusive here
print("Let's drop a particular column")
print(book.drop("age",axis=1))  # here axis=1  means we want to drop the column
print("Let's drop some rows")
print(book.drop([3,4,5,6],axis=0))      # here axis=0  means we want to drop rows
print("let's drop name column and 1,3 ,7 rows")
print(book.drop(("name"),axis='columns').drop([1,3,7],axis='rows'))

# instead of 1 and 0 you can mention 'columns' and 'rows' respectively

# Columns can be dropped at the time of reading itself.

print("\n")
cancel =['address','age']
book1=read_csv("Book2.csv").drop(cancel,axis='columns')
print(book1)
