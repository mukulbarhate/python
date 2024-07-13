from django.shortcuts import render
from . MyForm import InputForm
from django.http import HttpResponse


import mysql.connector as m

# database connectivity

mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")
query="insert into person(name,address,age) values(%s,%s,%s)"         #  must be "s"
cursor=mydatabase.cursor()

# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def result(request):
    form = InputForm(request.POST)
    cursor.execute(query,[form['name'].value(),form['address'].value(),form['age'].value()])     
    mydatabase.commit()
    return HttpResponse()
    
   