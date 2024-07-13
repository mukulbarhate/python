# --------------------- Dictionary --------------------------
# 1) accept 5 students name and store them in the dictionary by providing keys from 1 to 5 respectively.
# student={}
# for i in range(1,6):
#     name=input(f"Enter {i} name: ")
#     student[i]=name

# print(student)
s1={}
print(type(s1))

# 2) create a dictionary with pairs
# 	soap:100
# 	deo:300
# 	perfume:400

# now accept a product name from user (in any case, so you have to handle "ignore case") and display its price. Also , if the product is not present in the dictionary display the error message " product not available "
# 	Note:  you should not get "KeyError:" in the program.





# 3) define a class "Student" with members
# 	name,age,address and qualification
	
#    define parameterized constructor and "str" member function which returns all the members

#    create 4 objects of Student by passing values.

# now create a dictionary with rollno ( start from 1 ) as a key and student object as a value.

# accept a rollno from user and display all its details i.e. name,age,address and qualification.
# also display message "student not found" in case if rollno entered by user is not available as a key inside the dictionary.

# 4)  Given a dictionary of students and their favourite colours: 
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
# 1. Find out how many students are in the list 
# 2. Change Lisa’s favourite colour 
# 3. Remove 'Jenny' and her favourite color
# 4. Sort and print students and their favourite colours alphabetically by name





# ---------------------- TUPLE -----------------
# 1) Write a Python program to count the elements in a list until an element is a tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3
   


# 2) create a tuple to store 5 numbers and then sort it in ascending and descending order.

# 3) Write a Python program to find the repeated items of a tuple.



# ------------------------------ STRING ----------------------
# 1) accept a string and display whether it is palindrom or not.

"""
    n=input("Enter your string: ")
    if n[::-1] == n[0:]:
        print("It is Palindrom")
    else:
        print("It is not Palindrom")
"""



# 2) accept a string and display it. now accept slicing positions from and to , slice the string and display it.
# """
#     a1=input("Enter your string: ")
#     print(a1)
#     n1=int(input("Slicing two number from: "))
#     n2=int(input("Slicing two number to: "))
#     # print(type(n1))
#     print(a1[n1:n2])
# """



# 3) accept a string and display how many vowel characters are there inside it.
"""
    s1 = input("Enter string: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s1 if char in vowels)

    print(f"There are {count} vowels in this string")


    s1=input("Enter string: ")
    mylist=[]
    for i in range(0,s1.__len__()):
        mylist.append(s1[i])

    livowel=[]
    flag=0
    ifvowel=False
    for let in mylist:
        if let=='a' or let=='e' or let == 'i' or let=='o' or let=='u':
            ifvowel=True
            flag+=1
            livowel.append(let)
        else:
            ifvowel=False

    print(f"There are {flag} vowel in this string")
    """



    # 4) accept a string and display the characters which are repeated in the string


    # 5) accept a string and find out how many words are there in it.
"""
    str=input("Enter string and you will get the no. of words: ").split(" ")
    mylist=[]
    mylist.extend(str)
    words=0
    for i in range(0,mylist.__len__()):
        words+=1

    print(f"There are {words} in the string provided.")
    """



    # 6) accept a sentence and reverse it.
    # 	e.g.  hello world
    # 		world hello
"""
    s1=input("Enter your string: ").split()
    mylist=[]
    mylist.extend(s1[::-1])
    # for i in mylist:
    # print(mylist[0:])
    for i in range(0,mylist.__len__()):
        print(mylist[i],end=" ")
    """



    # 7) A pangram is a sentence that contains all the alphabets.
    # example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
# import re
# sent="The Quick Brown Fox Jumps Over The Lazy Dog"
# print(sent.span(" "))
# print(r[A-z])

