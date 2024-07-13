from turtle import color
from matplotlib import pyplot as py

data={"Action":60,"Romance":20,"Comedy":10,"Drama":10}

movies=list(data.keys())
no_of_people=list(data.values())

py.bar(movies,no_of_people,color='r')
py.xlabel("Types of movies")
py.ylabel("percentage of people like")
py.show()