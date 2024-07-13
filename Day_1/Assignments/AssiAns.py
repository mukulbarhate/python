# 19) print the following
#    J
#   A A
#  V V V
# A A A A
"""
li=['J','A','V','A']
for i in range(0,4):
    for k in range(0,3-i):
        print(" ",end="")
    
    for j in range(0,i+1):
        print(li[i],"",end="")
    print()
"""

# 18) print the following
#     A
#    B B
#   C C C
#  D D D D
# E E E E E 
"""
letter=65
for row in range(1,6):
    for spaces in range(1,6-row):
        print(" ",end="")
    for column in range(0, row):
        print(chr(letter),"",end="")
    letter+=1
    print()
"""

# 17) print the following
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# * * * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 
"""
for i in range(1,6):
    for j in range(0,6-i):
        print(end=" ")
    for k in range(0,i):
        print("* ",end="")
    print()

for i in range(0,6):
    for j in range(i):
        print(end=" ")
    for k in range(1,7-i):
        print("* ",end="")
    print()

"""

# 16) print the following pattern
# *   *   *   *   *   
#   *   *   *   *   
#     *   *   *   
#       *   *   
#         *   
"""
for i in range(0,6):
    for k in range(i):
        print(" ",end="")
    for j in range(1,7-i):
        print("*",end=" ")
    print()
"""


# 15) print the following pattern
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
"""
for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
        
    for k in range(0,i):
        print("*",end=" ")
    print()
"""


# 14) print the following pattern
# 		          *
# 	           *  *
#           *  *  *
#        *  *  *  *
#     *  *  *  *  *

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
        
#     for k in range(0,i):
#         print("*",end=" ")
#     print()

# 13) print the following pattern:
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()

----- OTHER WAY -----
for i in range(1,6):
    for j in range(1,6-i):
        print("*",end="")
    print()
    
"""




# 12) print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
"""
for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()
"""


# 11) accept a number and display whether it is prime or not
"""
n1=int(input("Enter ur number: "))
if n1>1:
    for num in range(2,n1):
        if (n1%num)==0:
            print("NON PRIME NUMBER")
            break
    else:
        print("PRIME NUMBER")
else:
    print("INVALID INPUT")
"""

# 10) display prime numbers from 3 to 30
"""
print("Prime numbers are: ")
for num in range(3, 31):
    for i in range(2, num):
        if (num%i)==0:
            break
    else:
         print(num)
"""

        
# 9) display fibonicii series of 10 numbers
# 0 1 1 2 3 5 8 13 21
# f s f+s
#   f  s f+s
#      f  s f+s
""""
first_num=0
second_num=1
print("Fibonicci Series: ",end="")
for i in range(0,10):
    sum=first_num+second_num
    print(f"{first_num}",end=" ")
    first_num,second_num=second_num,sum
    # first_num=second_num
    # second_num=sum
"""


# 8) accept a character and display whether it is upper case or lower case or not an alphabet.
""""
cha=input("Enter your char: ")
if cha.isalpha():
    if cha.isupper():
        print(f"Your character {cha} uppercase letter.")
    elif cha.islower():
        print(f"Your character {cha} lowercase letter.")
else:
    print(f"Your character {cha} is not an Alphabet.")
"""


# 7) accept numbers till user enters 0 and display the total of all the numbers entered.
"""
while True:
    num=int(input("Enter your number: "))
    if num==0:
        break
    else:
        print(num)
    num+=1

print("You entered number ZERO.")
"""


# 6) print the total of first 10 numbers.
""""
add=0
for no in range(1,11):
    add+=no
print(add)
"""


# 5)	accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
""""
marks=int(input("Enter your Total marks:\n"))
if marks<=100 and marks>=80:
    print("YOu got Distinction")
elif marks>=70:
    print("You got First Class")
elif  marks>=60:
    print("You got Second Class")
elif marks>=50:
    print("Pass")
else:
    print("Your are FAIL")
"""


# 4)	Display numbers from 3 to 30 except number 24  using while loop.
"""
n=3
while n<31:
    if n==24:
        n += 1
        continue
    print(n)
    n+=1
"""


# 3)	Display numbers  1 to 10 using  While loop
"""
i = 1
while i<11:
    print(i)
    i+=1
"""


# 2)	using switch ….case   display whether accepted character is vowel or not.
"""
def checkVowel(conv):
    print(f"Your character {conv} is a VOWEL")
char=input("Enter your character:\n")
conv=char.upper()
match conv:
    case 'A':
        checkVowel(conv)
    case 'E':
        checkVowel(conv)
    case 'I':
        checkVowel(conv)
    case 'O':
        checkVowel(conv)
    case 'U':
        checkVowel(conv)
    case _:
        print(f"Your character {conv} is consonent.")
"""

# 1)	accept a number and display its table.
"""
num=int(input("Enter your number for table: \n"))

for row in range(1,11):
    print(f"{num}x{row}={num*row}")
"""



