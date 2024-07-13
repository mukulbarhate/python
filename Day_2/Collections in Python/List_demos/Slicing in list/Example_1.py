# print(mylist[1::3]) will print every third element starting
# from the second element of mylist.

mylist=[10,20,30,40,50]
print(mylist)
print(mylist[:])
print(mylist[::])
print(mylist[1::2])  # print every second element from position 1
print(mylist[::2])   # print every second element from the beginning
print(mylist[2::2])   # print every second element from position 2
print(mylist[1:4])    # from position 1 to 3, 4 is exclusive
print(mylist[2:])     # from position 2 till end
print(mylist[:2])     # from position 0 till 1 , 2 is exclusive
print(mylist[-4:-1])  # from position -4 till -2  -1 is exclusive
print(mylist[::-1])   # print every element from the last
print(mylist[::-2])   # print every second element from the last
print(mylist[:1:-2])  # print every second element from the last till index 2
print(mylist[:1:-1])  # print every element from the last till index 2
print(mylist[:2:-1])  # print every element from the last till index 3
print(mylist[:2:-2])  # print every second element from the last till index 3
print(mylist[:2:2])   # print from 0 to 1 with the step 2