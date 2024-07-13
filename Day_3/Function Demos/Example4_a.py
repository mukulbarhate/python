# global and local variable
var=500     # Global variable

def disp():
    print("value of var is\t",var)

def myfun():
    var=100    # Local Variable
    print("value of var is\t",var)
    disp()
myfun()




