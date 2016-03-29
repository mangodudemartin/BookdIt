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
#REGISTRATION VIEW
def register(request):
    return render(request, 'bookdit/auth/register.html', {})

#LOGIN VIEW
def vlogin(request):
    return render(request, 'bookdit/auth/login.html', {})


# PROCESS LOGIN REQUEST
def login_request(request):
    try:    
        username = request.POST['login_username']
        password = request.POST['login_password']
        remember = request.POST.get('login_rememberme', 'off')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                if remember == 'on':
                    request.session.set_expiry(2592000)
                else :
                    request.session.set_expiry(0)
                    
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        
        
    except:
        return render(request, 'bookdit/auth/login.html', {
            'error_message': '#ERROR'
        })
    else:
        return render(request, 'bookdit/auth/login.html', {
            'error_message': "Incorrect Username and/or Password"
        })        


# PROCESS LOGOUT REQUEST
def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


