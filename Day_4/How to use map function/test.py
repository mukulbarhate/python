l = ['sat', 'bat', 'cat', 'mat']

test=list(map(list, l))
print(test)

for i in map(list,l):
    print(i)

for i in map(list,l):
    for j in i:
        print(j,end=" ")
    print("\n")
# def addition(n):
#     return n+n

# mytuple=(12,23,4,3)
# print(mytuple)
# print(type(mytuple))

# result=map(addition, mytuple)
# print(list(result))
# print(result)
# print(*result)
# print(list(result))
