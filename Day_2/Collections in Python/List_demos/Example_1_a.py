mylist = [10,20,30,40]
print(mylist)
print(type(mylist))
print("address of mylist is\t",id(mylist))
for i in range(0,len(mylist)):
    print("address of element\t",i,"\tis\t",id(mylist[i]))
print(mylist[0])
print(len(mylist))
mylist.append(50)   # list is dynamic
print("addresses after appending")
print("address of mylist is\t",id(mylist))
for i in range(0,len(mylist)):
    print("address of element\t",i,"\tis\t",id(mylist[i]))

print(mylist)
mylist[0]=12        # list is mutable
print("addresses after changing data")
print("address of mylist is\t",id(mylist))
for i in range(0,len(mylist)):
    print("address of element\t",i,"\tis\t",id(mylist[i]))
print(mylist)