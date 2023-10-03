from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):

    print(request.user.is_authenticated)

    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    else:
       return redirect('login') 
        
    
def login(request):
    return render(request, "dashboard/login.html")
    
