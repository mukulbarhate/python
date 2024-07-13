from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from .models import Employee

import mysql.connector as m

# database connectivity

mydatabase=m.connect(host="localhost",user="root",password="root",database="mydb")

cursor=mydatabase.cursor()


def home(request):
    return render(request,'home.html')
    
def viewpersons(request):
    query="select * from dept"
    cursor.execute(query)
    result=cursor.fetchall()  
    return render(request,'welcome.html',{'myresult':result})