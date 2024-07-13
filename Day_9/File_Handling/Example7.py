# how to write inside a file and read also using "w+" mode ( write and read mode)


with open("myfile.txt","w+") as f:
    print("enter messages, stop to quit\n")                         # write as well as read
    while True:
        str=input()
        if str=="stop":
            break
        f.writelines(str+"\n")
    f.seek(0, 0)  # place the file pointer at the beginning  second is default parameter
    data=f.read()
    print(data)
print("Done")

