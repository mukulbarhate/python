from django.shortcuts import render
from . MyForm import InputForm
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def result(request):
    form = InputForm(request.POST)
    print(form['name'].value(),"  ",form['address'].value(),"   ",form['age'].value())
    return HttpResponse(form['name'].value()+"   "+form['address'].value()+"    "+str(form['age'].value())) 
    
   