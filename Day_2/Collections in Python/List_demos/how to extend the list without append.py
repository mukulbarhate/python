
# how to extend the list without append
x = [10, 20, 30]
y = [40, 50, 60]
# x+=y
# print(x)

x[:0]=y    #from begining to 0th index
print(x)

x[2:]=y     #from 3rd to last
print(x)



