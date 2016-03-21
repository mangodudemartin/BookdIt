from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from bookdit.models import *

#----------------------------------------------------------------------------------------
#    USER AUTHENTICATION
#----------------------------------------------------------------------------------------
#LOGIN VIEW
def vlogin(request):
    return render(request, 'bookdit/home/login.html', {})


# PROCESS LOGIN REQUEST
def login_request(request):
    try:    
        username = request.POST['login_username']
        password = request.POST['login_password']
        print('username:',username)
        print('password:',password)
        
        user = authenticate(username=username, password=password)
        print('user.is_active:',user.is_active)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                #return render(request, 'bookdit/home/index.html', {})
                return HttpResponseRedirect(reverse('bookdit:index'))
        
        
    except:
        return render(request, 'bookdit/home/login.html', {
            'error_message': 'Incorrect Username and/or Password'
        })
    else:
        return render(request, 'bookdit/home/login.html', {
            'error_message': "OH! Busted!"
        })        


# PROCESS LOGOUT REQUEST
def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('bookdit:index'))


