num=[1,2,3,4,5,6,7]

# print(num)
# print(num[1])
# print(num[0:2])
# print(num[2:6])
# print(num[:])
# print(num[::])
# print(num[1::2])
print(num[:2:-2])

# userlist=[int(num) for num in input("Enter your numbers: ").split("*")]
# print("Number which are present are: ",userlist)

# a, b, c=[int(y) for y in input("Enter values").split()]
# print(a+69,"\t",b+69,"\t",c+69)

# a,b,c=input("Enter 3 numbers: ").split("-")
# print(a,"\t",b,"\t",c)

# rank=[99, 60, 90]
# hero=['a','g','h']
# rank.sort()

# for (a, b) in zip(rank, hero):
#     print(a,b)


# lis=['a','b','c','d','e']

# print(lis)
# print(type(lis))

# userval=input("Enter the char: ")
# if userval in lis:
#     print(userval," is in lis")
# else:
#     print(userval," is not in lis")

# print(userval," is at the ",lis.index(userval)," position")



# class Employee:
#     def __init__(self, eid, deptname,salary):
#         self.eid=eid
#         self.deptname=deptname
#         self.salary=salary
    
#     def __str__(self):
#         return str(self.eid)+"\t"+self.deptname+"\t"+str(self.salary)
    
#     def getname(self):
#         return self.deptname
#     def geteid(self):
#         return self.eid
#     def getsalary(self):
#         return self.salary
    
# e1=Employee(1, "HR", 1000)
# e2=Employee(20,"Fin",200)
# e3=Employee(3,"Mar",500)

# emplist=[e1,e2,e3]
# print(emplist)

# for i in emplist:
#     print(i)

# # emplist.sort()
# emplist.sort(key=Employee.getsalary,reverse=True)
# print("After sorting")

# for i in emplist:
#     print(i)


# a=[8,7,-9,7]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# c=[y for y in range(5,20) if y%4==0]
# print(c)

# nestlist=[["a",2,True],["z",4,False]]
# nestlist.remove(nestlist[0])
# nes = nestlist.append([[2,'a',3],[1,8,True]])
# nestlist.extend([20,True,"welcome"])
# # ness = nestlist.insert(2,[8,234])
# print(nestlist)


# die={1:"ab",2:"cx",8:"er"}
# for i in die:
#     print(i)
#     print(die[i])
# c={7, 96,78,7}
# print(c.add(99))
# print(c)


# tu=(5,6,7,8)
# print(tu.__add__((77,12,5)))

# li=[1,5,4,8]
# li.append(69)
# print(li)

# a='AcaD'
# print(a.swapcase())

# import array as ar

# a = ar.array('i',[1,2,3])   #  array    similar datatypes only, 
# print(a,"\t",id(a))
# a.append(30)   # arrays are mutable
# print(a,"\t",id(a))
# a[1]=22    # arrays are mutable
# print(a,"\t",id(a))