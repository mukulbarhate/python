from numpy import *

random.seed(8)
first=random.randint(1,500,30).reshape(6,5)     # reshape(no_rows,no_col)
print("array created is")
print(first)
# [[452 341 498 362 134]
#  [475 137 340 361 192]
#  [ 49 366  86 317 434]
#  [116 459 156 109 270]
#  [394  62 144 350 355]
#  [316  19 271 103 350]]

print("from the 2nd row")
print(first[2:])            #  from 2nd row
# [[ 49 366  86 317 434]
#  [116 459 156 109 270]
#  [394  62 144 350 355]
#  [316  19 271 103 350]]

print("\n")
print(first[2:,3])          #  from 2nd row and only 3rd column
# [317 109 350 103]

print("\n")
print(first[2:,2:])         #  from 2nd row and from 2nd column
# [[ 86 317 434]
#  [156 109 270]
#  [144 350 355]
#  [271 103 350]]

# let's extract  459  62  and 19
print("\n")
print(first[3:,1:2])
# [[459]
#  [ 62]
#  [ 19]]

# let's extract 340 361 86 317 156 and 109
print("\n")
print(first[1:4,2:4])
# [[340 361]
#  [ 86 317]
#  [156 109]]

print("\n")
# let's extract  459  156  and 109
print(first[3:4,1:4])
# [[459 156 109]]