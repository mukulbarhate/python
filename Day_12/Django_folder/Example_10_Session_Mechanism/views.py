
from django.shortcuts import render,HttpResponse


def home(request):
    return render(request,'home.html')
    
def shop(request):
    return render(request, 'shop.html')

def addCart(request):
    items = request.POST.getlist('product')
    if request.session.get("prodlist"):
        mylist=request.session.get("prodlist")
        mylist.extend(items)
        request.session['prodlist']=mylist
    else:
        request.session['prodlist']=items
    return render(request, 'home.html')
    

def viewCart(request):
    if request.session.get("prodlist"):
        mylist=request.session.get("prodlist")
        return render(request, 'viewCart.html',{'itemlist':mylist})
    else:
        return render(request,'Empty.html')

def payment(request):
    # as if we receive payment here
    del request.session['prodlist']  # to kill the session
    return render(request, 'welcome.html')

   