from numpy import *

print("enter from which number")
start=int(input())
print("enter till which number")
end=int(input())
print("enter how many numbers")
total=int(input())
first=linspace(start,end,total)
print(first)