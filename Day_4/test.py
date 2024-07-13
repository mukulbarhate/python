def myfun(fun,*val):
    fun(val)
multiple=lambda *arg:[print(i) for i in arg]
myfun(multiple,10,"Hell",69)

# def myfun(fun, num):
#     fun(num)
# disp=lambda x:[print(i) for i in range(1,x)]
# myfun(disp,7)

# def myfun(fun):
#     fun()

# temp=lambda:print("Welcome to lambda function")
# myfun(temp)

# myfun(lambda:print("This is another lambda"))

# (lambda:print("Welcome to lambda world"))()
# print((lambda x: x*x)(10))

# add=lambda x,y:x+y
# print("add is the reference to the object of type\t",type(add))
# print("address of the object where add refers to is\t", id(add))
# print(add(5,6))

# makecube = lambda val: val**3
# myval=int(input("enter number to calculate the cube"))
# print(makecube(myval))
