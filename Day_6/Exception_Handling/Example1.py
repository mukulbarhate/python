var=5
try:
    print(var/0)
except ZeroDivisionError:
# except Exception:     # you can also use this as except
    print("You can't divide any number by 0")
print("done")
