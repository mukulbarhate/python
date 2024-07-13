# 11) accept a number and display whether it is prime or not

num=int(input("Enter your number: "))
for i in range(3, num+1):
    if num%i==0:
        isPrime=False

isPrime=True


if isPrime==True:
    print("It is prime")
else:
    print("It is not prime")


# 10) display prime numbers from 3 to 30
# num=2
# for i in range(3, 31):
#     if num%2==0 and i:
#         print(num)
#         num+=1
#     num+=1

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
    first_num=second_num
    second_num=sum
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



