


#----------- Instance Method class method static method ---------------
# class Account:
#     rate=9
#     def __init__(self,accid,name,balance):
#         self.accid=accid
#         self.name=name
#         self.balance=balance
#     def getAccid(self):
#         return self.accid
#     def getName(self):
#         return self.name
#     def getBalance(self):
#         return self.balance
#     @classmethod
#     def getRate(cls):
#         return cls.rate
#     @staticmethod
#     def calculateEMI(no_of_years,loan_amt):
#         return "calculate EMI per month"
    
# c1=Account(1,"Abc",40000)
# c2=Account(2,"Xyz",70000)
# print(c1.getAccid(),"\t",c1.getName(),"\t",c1.getBalance())
# print(c2.getAccid(),"\t",c2.getName(),"\t",c2.getBalance())
# print(Account.getRate())
# print(Account.calculateEMI(10,200000))

#------------instance variable --------
# class Account:
#     rate=9
#     def __init__(self,accid, name, balance):
#         self.accid=accid
#         self.name=name
#         self.balance=balance

# c1=Account(1,"XYZ", 40000)
# c2=Account(2,"PQRS",600)
# print(c1.accid,"\t",c1.name,"\t",c1.balance)
# print(c2.accid,"\t",c2.name,"\t",c2.balance)

# c1.balance=2578
# c2.balance=988
# print(c1.accid,"\t",c1.name,"\t",c1.balance)
# print(c2.accid,"\t",c2.name,"\t",c2.balance)
# print(Account.rate,"\t",c1.rate,"\t",c2.rate)

# Account.rate=12
# print(Account.rate,"\t",c1.rate,"\t",c2.rate)
# print(id(c1.name),"\t",id(c2.name))




#---------- CLASS VARIABLE -------------
# class First:
#     var=20
# f1=First()
# f2=First()

# print(First.var)
# print(f1.var)
# print(f2.var)

# print(id(First.var))
# print(id(f1.var))
# print(id(f2.var))


#---------- Duck Typing -----------------
# class Bird:
#     def fly(self):
#         print("Bird is flying")

# class SuperMan:
#     def fly(self):
#         print("Superman is flying")

# class Person:
#     def talk(self):
#         print("Person is flying")

# def perform(obj):
#     print("Type of obj is \t",type(obj))
#     if(hasattr(obj,"fly")): # Strong Typing which is checked before entering
#         obj.fly()
#     else:
#         print("Can't fly")

# b1=Bird()
# perform(b1)
# s1=SuperMan()
# perform(s1)
# p1=Person()
# perform(p1)



# ---------- Class Object ------------
# class Test:
#     x=10
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# ref=Test
# print(dir(ref))

# ref1=Test
# print("\n")
# print(id(ref)==id(ref1))
# t1=Test(10,20)
# t2=Test(40,50)
# print('\n')
# print(dir(t1))
# print("\n")
# print(id(t1)==id(t2))


# ------------Garbage Collection------------
# class Myclass:
#     var=0
#     def __init__(self, var):
#         self.var=var
#     def getvar(self):
#         return self.var
#     def __del__(self):
#         print("No Referene is left for {}".format(self))

# m1=Myclass(10)
# print(id(m1))
# print(m1.getvar())
# m2=m1
# print(id(m1))
# print(m1.getvar())
# del m1
# print("After deleting m1",m2.getvar())
# print("Done")



# var=100
# print(var)
# del(var)
# print(var)

# class First:
#     def mainfunction(self):
#         print("Adress of self",id(self))
#         print("type of self",type(self))
#         print("inside main function")

# f1=First()
# print("Address of f1 ",id(f1))
# f1.mainfunction()

# f2=First()
# print("Address of f2is\t",id(f2))
# f2.mainfunction()

# class Student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
    
#     def getname(self):
#         return self.name

#     def getage(self):
#         return self.age

#     def __str__(self):
#         return self.name+"\t"+str(self.age)
    
# s1=Student("Pratik", 25)
# s2=Student("David",56)

# print(s1.getname(),"\t",s1.getage())
# print(s2.getname(),"\t",s2.getage())

# print(s1)
# print(s2)