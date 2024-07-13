""" In Python, there's no tuple comprehension.
However, you can mimic the tuple comprehensions by running a generator expression inside tuple() function call. 
 """
mytuple=(i for i in range(1,10))   # you are trying to do Set Comprehension
print(mytuple)  # it is a generator not a tuple
mytuple1=tuple(i for i in range(1,10))  # we are converting generator to tuple
print(mytuple1)    # it's a tuple now
print(type(mytuple1))
