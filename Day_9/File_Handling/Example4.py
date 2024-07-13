
# we can define which specific file to include under archive. 


from zipfile import ZipFile

with ZipFile("temp.zip","w") as newzip:
		newzip.write("D:\PG-DBDA CDAC\Python\lectures\Day_8\JupyterNotebook\Book1.csv")
		newzip.write("D:\PG-DBDA CDAC\Python\lectures\Day_8\JupyterNotebook\ForPandas.xls") 

""" 
newzip=ZipFile("temp.zip","w")
try:
    newzip.write("Book1.csv")
    newzip.write("ForPandas.xls")
finally:
    newzip.close() 
"""

print("Done")

