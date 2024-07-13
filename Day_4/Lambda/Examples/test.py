# myfun2=lambda **values:[print(key,":",value) for key,value in values.items()]
# myfun2(name="Rohit",age=69,address="PUne")

# myfun= lambda *values:[print(i) for i in values]
# myfun(1,7,8,9)

# def myfun(*values):
#     for i in values:
#         print(i)
# myfun(10,50,60)

# animals=['cat', 'dog','parrot']
# uppered_animal=list(map(lambda animal:animal.upper(), animals))


# my_list=[20,48,56]
# new_list=list(map(lambda x: x*2, my_list))
# print(new_list)

# temp1=lambda *x:[print("no args passed to lambda") if(len(x)==0) else [print(i) for i in x]]
# temp1()
# temp1(300)
# temp1(500,900)

# min = lambda a, b : a if(a<b) else b
# print(min(100, 600))

# min1=(lambda a,b: a if(a<b) else b)(50,60)
# print(min1)

# def myfun(fun,*val):
#     fun(val)
# multiple=lambda *args:[print(i) for i in args]

# myfun(multiple, 30,60,90,99)

# def myfun(fun,num):
#     fun(num)
# disp=lambda x:[print(i) for i in range(1,x)]

# myfun(disp,7)

# passing lambda as an argument
# def myfun(fun):
#     fun()
# temp=lambda:print("Welcome to lambda world")
# myfun(temp)

# myfun(lambda:print("Thsi the other dimension"))

# (lambda:print("Welcome to lambda world"))()

# print((lambda x: x*x)(50))

# disp=lambda:[print("Welcome"),print("HI"),print("Good bye")]
# print("Disp reference ",type(disp))
# print("Address of object", id(disp))
# disp()

# disp=lambda:print("welcome")
# print("disp is the reference to the object of type\t",type(disp))
# print("address of the object where disp refers to is\t", id(disp))
# disp()

# disp=lambda : print("Welcome")
# print("display the reference of object",type(disp))
# print("address of object ",id(disp))
# disp()

# add=lambda x,y:x+y
# print("add is reference ",type(add))
# print("address if object ",id(add))
# print(add(9,8))

# makesquare=lambda val: val**2
# myval=int(input("Enter your number for square: "))
# print(makesquare(myval))


# mystring ='Pranesh'
# makeupper=lambda val: val.upper()

# print(makeupper(mystring))