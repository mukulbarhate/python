# default arguments of the function

def disp(var1,var2=20):		# var2 - default argument it will override 20
	print(var1,"\t",var2)
	
def fun():
	disp(10)
	disp(100,200)
fun()


