# urDict={9:'z',1:'b',8:'e'}
# print(urDict[9])
# for i in urDict:
#     print(urDict[i])



""" In Python, there's no tuple comprehension.
However, you can mimic the tuple comprehensions by running a generator expression inside tuple() function call. 
 """
# mytuple=(i for i in range(1,10))   # you are trying to do Set Comprehension
# print(mytuple)  # it is a generator not a tuple
# mytuple1=tuple(i for i in range(1,10))  # we are converting generator to tuple
# print(mytuple1)    # it's a tuple now
# print(type(mytuple1))


# Set Comprehensions
# myset={x for x in range(1,11)}
# print(myset)
'''
mydictionary={'soap':100,'perfume':50,'Deo':200}
myset={x for x in mydictionary.values()}
print(myset)

myset1={x for x in mydictionary.keys() if len(x)>3}
print(myset1)
'''


# List Comprehensions
# It is used to create new list from other iterable like tuples, strings, arrays,lists

# mylist=[i for i in range(4,20) if i%2==0]
# print(mylist)

# mylist=[num**2 for num in range(1,16,2)]
# print(mylist)

# Dictionary Comprehension
# mydict={x:x**3 for x in range(1,11)}
# for i in mydict:
#     print(i," ",mydict[i])

# product=['Soap','Perfume','Deo','Hair oil']
# prices=[100,200,150,500,120]
# mydict={key:value for (key,value) in zip (product,prices)}
# for i in mydict:
#     print(i," ",mydict[i])

# List Comprehension squares of number from 0-9
# print([x**2 for x in range(10)])

# Dictionary Comprehension square of number from 0-9
# print({x:x**2 for x in range(10)})

# Set Comprehension to create a set of unique first letters form a list of words
# print({word[0] for word in ['apple','banana','cherry']})

# Comprehension not allowed in Tuples

# Generator Comprehensions
# input_list=[1,2,3,4,5,6,6,7,8.8]
# ouput_gen=(var for var in input_list if var%2==0)
# print(ouput_gen)
# print("Output values using generator comprehensions: ",ouput_gen,end="")