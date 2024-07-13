# 1) create a list , accept a number,name and a float value from user and store it inside the list. now accept one more name from user and insert it at 2nd position. accept a number and append it at the end of the list.print the entire list.
"""
l1=[]
num=int(input("Enter number: "))
nam=input("Enter name: ")
flo=float(input("Enter float: "))
l1=[num,nam,flo]
nam2=input("Enter other name: ")
l1.insert(2, nam2)
num1=int(input("Enter number: "))
l1.append(num1)
print(l1)
"""

# 2) first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length.
"""
l1=[]
while True:
    num1=int(input("Enter your number: "))
    if num1 == 0:
        break
    l1.append(num1)

print(l1)
print(l1.__len__())
"""



# 3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.
"""
mylist=[int(x) for x in input("Enter your number").split()]
print(mylist)
n1,n2,n3,n4,n5=[int(x) for x in input("Enter 5 numbers: ").split()]
l1=[n1,n2,n3,n4,n5]
print("Your list is",l1)
nn1,nn2,nn3=9,99,999
l1.extend([nn1,nn2,nn3])
print(l1)
"""

# 4) accept a number,string,decimal,boolean value and a character from the user and store it inside the list. First print the list from the beginning and then from the end.
"""
lis=[]
n1=int(input("Enter your number: "))
s1=input("Enter your string: ")
d1=float(input("Enter your decimal no.: "))
b1=bool(input("Enter your boolean value: "))
ch1=input("Enter your character: ")
lis.extend([n1,s1,d1,b1,ch1])
print(lis[0:])
print(lis[::-1])
"""


# 5) accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove from the list and  after removing it, display the list.
""""
l1=[]
n1,n2,n3,n4,n5=[num for num in input("Enter 5 numbers: ").split()]
l1.extend([n1,n2,n3,n4,n5])
nn1=input("Enter number to be remove: ")
l1.remove(nn1)
print(l1)
"""


# 6) accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that position and  after removing it, display the list.

""""
l1=[]
n1, n2, n3, n4, n5=[num for num in input("Enter 5 numbers: ").split()]
l1.extend([n1,n2,n3,n4,n5])
nn1=int(input("Enter position you want to delete: "))
l1.pop(nn1)
print(l1)
"""

# 7) create a list and store string,number,character,boolean,decimal values respectively inside it.
# Now slice it in following ways:
# a) display it in reverse order
# b) list all the elements from 2nd position
# c) list the elements from 1st to 3rd position
# d) slice it from 1st to 3rd elements from the end.
"""
# l1=[4,5,6,7,8,9,2]
# print(l1[:-4:-1])
l1=[]
s1=input("Enter your string: ")
n1=int(input("Enter your number: "))
ch1=input("Enter your character: ")
b1=bool(input("Enter your boolean value: "))
d1=float(input("Enter your decimal no.: "))
l1.extend([s1,n1,ch1,b1,d1])
print(l1)
print(l1[::-1])
print(l1[1:])
print(l1[0:2])
print(l1[:-4:-1])
"""





# 8) Note: use List comprehension create a list with the numbers from 1 to 20 create one more list which should contain only odd numbers from the first list.
"""
mylist=[int(n1) for n1 in range(0,20)]
newlist=[int(n2) for n2 in mylist if n2%2!=0]
print(mylist)
print(newlist)
"""



# 9) accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.
"""
l1=[]
n1, n2, n3, n4,n5=[name for name in input("Enter 5 names: ").split()]
l1.extend([n1,n2,n3,n4,n5])
l1.sort()
print("Ascending order: ",l1)
l1.sort(reverse=True)
print("Descending order: ",l1)
"""



# 10) create a class "Car" with two instance members i.e. "model(string)" and "isautomatic(boolean)" have getter methods also. create 5 to 6 objects by passing model name and True or False for "isautomatic". create a list and store all the objects inside it. now create one more list and in that list store all the objects from first list where "isautomatic" is True.Print both the lists.

"""
class car:
    def __init__(self, model, isautomatic):
        self.model=model
        self.isautomatic=isautomatic

    def __str__(self):
        return self.model+"\t"+str(self.isautomatic)

    def getmodel(self):
        return self.model
    def getisautomatic(self):
        return self.isautomatic

o1=car("BMW", True)
o2=car("Merce", True)
o3=car("Ferr", False)
o4=car("Bugga", True)
o5=car("Pors", True)

mylist=[o1,o2,o3,o4,o5]
print(mylist)

for i in mylist:
    print(i)
"""

