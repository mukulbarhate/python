class Car:
    def __init__(self,name, speed):
        self.name=name
        self.speed=speed
    def __str__(self):
        return ""+self.name+" "+str(self.speed)
    def getname(self):
        return self.name
    def getspeed(self):
        return self.speed
    
v2=Car('Buggatti', 400)
v1=Car('BMW',200)
v3=Car('Mustang',330)

cars={v1:1,v2:2,v3:3}

# for i in cars:
#     print(i)

# According to name
# nlis=sorted(cars, key=Car.getname)
# print(type(nlis))
# for i in nlis:
#     print(i)

# According to speed
splis=sorted(cars,key=Car.getspeed)
for i in splis:
    print(i)

# Descending order
# urdict={110:'John',101:'Ron',102:'Harry',103:'Hermione',105:{1:'Books', 2:'Potion',3:'Magic'}}



# sortlist=sorted(urdict,key=urdict.values())
# for i in sorted:
#     print(i)

# Take Multiple Inputs
# while 1:
#     key=int(input('Enter key: '))
#     if key == 0:
#         break
#     value=input('Enter value: ')
#     urdict[key]=value


# for i in urdict:
# print(urdict)


# urDict[104]='Pheonix'       # add a pair of key & value in Dictionary
# print(urDict)

# print(urDict[105][1])
# print(urDict[105][2])

# urDict[105][3]='Battle'       # updating value of a particular key in the nested dictionary
# print(urDict)

# print(type(urDict))

# print(urDict[103])

# urDict[100]='Hagrid'
# print(urDict)

# print(urDict.keys())
# print(urDict.values())