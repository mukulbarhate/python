# 1) define 3 functions "add()","modify()" and "delete()" with just a print message. now accept input from user as a number. if the number entered is 1, call "add()" if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
 
# def add():
#     print("ADD")
# def modify():
#     print("MODIFY")
# def delete():
#     print("DELETE")

# ent=int(input("Enter your input 1->add, 2->modify, 3->delete: "))
# match ent:
#     case 1:
#         add()
#     case 2:
#         modify()
#     case 3:
#         delete()
#     case _:
#         print("INVALID INPUT")

# 2) define a function which accepts a number and return its square.

# def sqr(num):
#     print(f"Square of {num} is",num**2)

# n=int(input("Enter your number: "))
# sqr(n)

# 3) define a function which accepts character,int,string and display them.

# def inpu(*vars):
#     for i in vars:
#         print(i)
# a1=input("Enter character: ")
# a2=int(input("Enter number: "))
# a3=str(input("Enter string: "))
# inpu(a1,a2,a3)

# 4) define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function. invoke myfun2()

# def myfun1():
#     print("myfun1")

# def myfun2():
#     print("myfun2")
#     myfun1()

# myfun2()

# 5) define a function to accept a number. This function should return 1 if a number passed is more than 0 return -1 if a number passed is less than 0 , else it should return 0.

# def accept(num):
#     if num>0:
    
#         return 1
#     elif num<0:
#         return -1
#     else:
#         return 0
    
# n=int(input("Enter number: "))
# # accept(n)
# print(accept(n))

# 6) define a function which accepts a character and return toggle of it. 

# def toggle(st):
#     if st.islower() == True:
#         print(st.upper())
#     else:
#         print(st.lower())

# n=input("Enter character to toggle: ")
# toggle(n)

# 7) define a function which accepts a string , toggle and return it.
# 	[ hint :  use "swapcase()" function of string ]

# def tog(st):
#     print(st.swapcase())

# name=input("Enter your string: ")
# tog(name)

# 8) write a function to accept minimum 3 characters and maximum 5 characters. 
#  	[ use default arguments method ]

# def nuu(c1,c2,c3,c4='m',c5='l'):
#     print(c1,c2,c3,c4,c5)

# n1=input("Enter character: ")
# n2=input("Enter character: ")
# n3=input("Enter character: ")
# n4=input("Enter character: ")
# n5=input("Enter character: ")
# nuu(n1,n2,n3)
# nuu(n1,n2,n3,n4)
# nuu(n1,n2,n3,n4,n5)


# 9) define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]
def nu(*vars):
    print(vars=vars+1)

n=int(input("Enter your numbers: ").split())
li
