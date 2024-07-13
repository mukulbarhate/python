# create a hierarchy
# 				Course

# 					void start()
# 					void end()

# override "start()" and "end()" in all the child classes.

# 		MsCit		Basic		Dbda
# 							void orientation()

# write a function "perform"
# 	perform function should be defined in such a way that it can accept any course and invoke "start()" and "end()" functions.
# 	also make sure if "Dbda" is passed , its "orientation()" method also should be called.


class Course:
    def start(self):
        print("Course is started")
    def end(self):
        print("Course is ended")
    
class MsCit(Course):
    def start(self):
        print("Course MsCit started")
    def end(self):
        print("Course MsCit is ended")

class Basic(Course):
    def start(self):
        print("Course Basic started")
    def end(self):
        print("Course Basic is ended")

class Dbda(Course):
    def start(self):
        print("Course Dbda started")
    def end(self):
        print("Course Dbda is ended")
    def orientation(self):
        print("The Orientation is going to start")
    
def perform():
    
c1=MsCit()
c1.start()
c1.end()