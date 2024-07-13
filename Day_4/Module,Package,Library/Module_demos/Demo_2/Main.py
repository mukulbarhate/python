# advantage of using (from First import disp1,disp2 __ from second import fun2)  is we can directly call the funtion which are there in the different module
from First import disp1,disp2
from Second import fun2


disp1(100)
disp2(300)
print(fun2())


