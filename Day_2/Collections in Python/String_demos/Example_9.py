# how to ignore cases in Python

mystring1 = "hello"
mystring2 ="Hello"

if(mystring1==mystring2):
    print("casewise they are equal")
else:
    print("casewise they are not equal")

if(mystring1.casefold()==mystring2.casefold()):
    print("after ignoring cases they are equal")
else:
    print("even after ignoring cases they are not equal")