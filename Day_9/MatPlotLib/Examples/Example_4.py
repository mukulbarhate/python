# Bar plot
from matplotlib import pyplot as py

students={"Rutik":90,"Sahil":80,"Suresh":70}

names=list(students.keys())
marks=list(students.values())

# py.bar(names,marks)
py.barh(names,marks)
py.ylabel("Students names")
py.xlabel("marks in maths")
py.show()

