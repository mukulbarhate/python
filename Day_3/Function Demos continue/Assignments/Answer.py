# 1) create 3 functions "show1()","show2()" and "show3()" now define a function "caller" in such a way that it can accept any function as an argument and invoke the same. invoke caller function by passing show1,show2 and show3


# 2) define nested function and show how will you invoke it.

def outer():
    num=100
    def inner():
        print("Your are inner",num)
    num=100
    print("You are outside")
    return inner

v1=outer()
v1()

