# There are two ways to slice the string

mystring = 'Vidyanidhi'
          # 12345678910
        #  10987654321
 
# Using slice constructor  , slice is an in-built class

s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -8, -2)
# s4=slice(1,6,-2)    # cannot give negative value here
# s4=slice(-2,-7,2)   # cannot give positive value here
s4=slice(-8,6)
# s5=slice(7,-8)   # requires negative value for step
s5=slice(7,-8,-1)
s6=slice(3,-3)
s7=slice(6,-7,-2)
s8=slice(6,-7,-1)
s9=slice(7,2,-2)
s10=slice(-7)    #  0 to -8


print(mystring[s1])
print(mystring[s2])
print(mystring[s3])
print(mystring[s4])
print(mystring[s5]) 
print(mystring[s6])
print(mystring[s7])
print(mystring[s8])
print(mystring[s9])
print(mystring[s10])

print("String slicing without slice class")

print(mystring[:3])  # or mystring[0:3]
print(mystring[1:5:2])
print(mystring[-1:-8:-2])
print(mystring[-8:6])
print(mystring[7:-8:-1])
print(mystring[3:-3])
print(mystring[6:-7:-2])
print(mystring[6:-7:-1])
print(mystring[7:2:-2])
print(mystring[:-7])   #  0 to -8
print(mystring[:])   # copy of the string
print(mystring[4:])
print(mystring[:-1])
print(mystring[::-1])
