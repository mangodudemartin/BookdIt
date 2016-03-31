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

def register_request(request):
    try :
        username = request.POST['login_username']
        password = request.POST['login_password']
        first_name = request.POST['login_first_name']
        last_name = request.POST['login_last_name']
        email = request.POST['login_email']
        
        #create the primary User model object in the database (builtin Django method)
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        
        #create the new custom User Profile model from the User model
        new_user_profile = userprofile()
        new_user_profile.user = new_user
        new_user_profile.save()
        
        return HttpResponseRedirect(reverse('vlogin'))
    except Exception as e:
        return render(request, 'bookdit/auth/register.html', { 'error_message' : str(e) })


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


