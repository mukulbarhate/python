class First:
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,obj):
        print("inside __add__ method of First")
        return self.num1+obj.num2
    def __sub__(self,obj):
        print("inside __mul__ method of first")
        return self.num1-obj.num2

class Second:
    def __init__(self,num2):
        self.num2=num2
    def __add__(self,obj):
        print("inside __add__ of num2")
        return self.num2+obj.num1

f1=First(100)
f2=Second(200)

print(f1.num1,"\t",f2.num2)
print(f1+f2)     # f1.__add__(f2)      
print(f2+f1)   # won't work