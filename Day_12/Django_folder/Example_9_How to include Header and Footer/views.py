from django.shortcuts import render

from django.http import HttpResponseRedirect


def home(request):
    return render(request, "home.html")

def national(request):
    return render(request, "National.html")

def international(request):
    return render(request, "International.html")


   