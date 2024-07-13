# 1) write a function to accept a number and return its square using
# 	a) normal function
# 	b) lambda

# def sqr(num):
#     return num**2

# print(sqr(4))

# val=int(input("Enter no.: "))
# sqr=lambda val:print(val**2)
# sqr(val)
# print("sqr is",(lambda val:(val**2))(val))

# 2) write a function to display "Hello World" using
# 	a) normal function
# 	b) lambda

# def disp():
#     print("Hello world")

# disp()

# (lambda:print("Hello World"))()
# val=lambda:print("hello World")
# val()


# 3) write a function with 2 arguments , second argument should be "default argument" and display them. Using
# 	a) normal function 
# 	b) lambda

# def take(n1,n2=69):
#     print("numbers are: ",n1," ",n2)
# take(96)

# value=lambda n1,n2=69:print("numbers are: ",n1," ",n2)
# value(78,100)

# (lambda n1,n2=69:print("numbers are: ",n1," ",n2))(89,800)

# 4) write a function with variable no. of arguments and display them. Using
# 	a) normal function
# 	b) lambda

# def vari(*var):
#     for i in var:
#         print(i)

# vari(5,"a",8)

# vari=lambda*var:[print(i) for i in var]
# vari(5,"a","p",8)

# (lambda*var:[print(i) for i in var])(5,"a","p",8)


# 5) write a lambda to reverse the given string

# str=lambda x:print(x[::-1])

# strin=input("Enter ur string: ")
# str(strin)


# 6) Given

# mylist=[10,20,30,(40,50,60),70,80]

# write a lambda expression to print the tuple from the list



# 7) write lambda expression to sort any given list in a descending order.



# 8) write a lambda expression to print those characters from a given string which ascii value is more than 110.

# 9) write a lambda to print every alternate character of a given string

# 10) Given

# prnnos=[1,2,3,4,5]
# names=["Rahul","Rohit","Sachin","Anil","Saurav"]

# write a lambda expression which creates a dictionary which consists of "prnnos" as keys and "names" as values.

# 11) accept a character and using lambda print whether it is upper case or lower case or not an alphabet.



