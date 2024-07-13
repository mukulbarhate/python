from matplotlib import pyplot as py

modules=['Java','Python','Javascript','C#']
popularity=[40,30,20,10]

py.pie(popularity,labels=modules,autopct='%0.1f%%',colors=['red','blue','yellow','pink'])
py.show()