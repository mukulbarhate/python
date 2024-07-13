a={1:'l' ,2:'m'}
b={3:'k' , 4:'j'}

dict.
print(a)

#--------Constructor overriding --------
# Hierarchical Inheritance
# class Base:
#     def disp1(self):
#         print("Base class disp1")

# class Sub1(Base):
#     def disp2(self):
#         print("Sub1 class disp2")

# class Sub2(Base):
#     def disp3(self):
#         print("Sub2 class disp3")

# s1=Sub1()
# s1.disp1()
# s1.disp2()
# s2=Sub2()
# s2.disp1()
# s2.disp3()

# Mutlilevel Inheritance Example 10
# class Base:
#     def disp1(self):
#         print("Base class disp1")

# class Sub1(Base):
#     def disp2(self):
#         print("Sub1 class disp2")

# class Sub2(Sub1):
#     def disp3(self):
#         print("Sub2 class disp3")
    

# s2=Sub2()
# s2.disp1()
# s2.disp2()
# s2.disp3()

# Example 9
# class Base:
#     def __init__(self,num1):
#         self.num1=num1
#         print("Base class constructor", self.num1)
    
#     def disp1(self):
#         print("Base class disp1 method")

# class Sub(Base):
#     def __init__(self):
#         super().__init__(900)
#         print("Sub class constructor")

#     def disp1(self):
#         super().disp1()
#         print("Sub class disp1 method")

# s1=Sub()
# s1.disp1()


# Example 8 Method overriding
# class Base:
#     def __init__(self,num1):
#         self.num1=num1
#         print("Base class constructor",self.num1)
#     def disp1(self):
#         print("Base class disp1 method")

# class Sub(Base):
#     def __init__(self):
#         super().__init__(500)
#         print("Sub class constructor")
#     def disp1(self):
#         print("Sub disp1 method")

# s1=Sub()
# s1.disp1()


# Example 6 & 7 We don't have method overloading in Python
# class Base:
#     def __init__(self,num1):
#         self.num1=num1
#         print("Base class constructor", self.num1)
#     def disp1(self):
#         print("Base class disp1 method")

# class Sub(Base):
#     def __init__(self):
#         super().__init__(500)
#         print("Sub class constructor")

#     def disp1(self,val1):
#         print("Sub class disp1 method", val1)

# s1=Sub()
# print(id(s1))

# s1.disp1(500)

# Example 5
# class Base:
#     def __init__(self, num1):
#         self.num1=num1

# class Sub(Base):
#     def __init__(self, num1,num2):
#         super().__init__(num1)
#         self.num2=num2
#     def show(self):
#         print(self.num1,"\t",self.num2)
    
# s1=Sub(50,45)
# s1.show()



# Example 4
# class Base:
#     def __init__(self,n1):
#         self.n1=n1
#         print("Base class constructor")

# class Sub(Base):
#     def __init__(self, n2):
#         super().__init__(n2+50)
#         self.n2=n2
#         print("Sub class constructor")

# s1=Sub(20)
# print(id(s1))
# print("base",s1.n1)
# print("sub",s1.n2)

# Example 3
# class Base:
#     def __init__(self):
#         print("Base class constructor")

# class Sub(Base):
#     def __init__(self):
#         print("Sub class constructor")
#         super().__init__()
    
# s1=Sub()
# print(id(s1))
# print(s1.__class__.__base__)
# print(s1.__class__.__base__.__base__)



# Example 1&2
# class Base:
#     def __init__(self):
#         self.num1=20
#         print("Baase class constructor")
#     def disp(self):
#         print("in base disp")
    
    
# class Sub(Base):
#     def __init__(self,num2):
#         super().__init__()
#         self.num2=num2
#         print("Sub class constructor")

# s1=Sub(100)
# print(id(s1))
# print(s1.__class__.__base__)
# print(s1.__class__.__base__.__base__)
# print(s1.num2)
# print(s1.disp)