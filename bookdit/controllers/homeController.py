from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from bookdit.models import *

#----------------------------------------------------------------------------------------
#    LOAD THE MAIN HOME SCREEN
#----------------------------------------------------------------------------------------
def index(request):
    if request.user.is_authenticated():
        context = {
            'current_username': request.user.username
        }
        return render(request, 'bookdit/home/index.html', context)
    else :
        context = {}
        return render(request, 'bookdit/home/login.html', context)


#----------------------------------------------------------------------------------------
#    PROCESS A LOGIN REQUEST
#----------------------------------------------------------------------------------------
def login(request):
    try:
        username = request.POST['login_username']
        password = request.POST['login_password']
        
        user = authenticate(username=username, password=password)
        
        
        if user is not None:
            if user.is_active:
                login(request, user)
                # return render(request, 'bookdit/home/index.html', {})
                index(request)
        
        
    except:
        return render(request, 'bookdit/home/index.html', {
            'login_return_message': 'Something went wrong, man!'
        })
    else:
        return render(request, 'bookdit/home/index.html', {
            'login_return_message': "Not sure what happened!!!! lol!"
        })
        

#----------------------------------------------------------------------------------------
#    PROCESS A LOGOUT REQUEST
#----------------------------------------------------------------------------------------
def logout_view(request):
    logout(request)
    return render(request, 'bookdit/home/login.html', {})

















