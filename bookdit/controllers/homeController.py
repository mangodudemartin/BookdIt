from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from bookdit.models import *


#----------------------------------------------------------------------------------------
#    LOAD THE MAIN HOME VIEW
#----------------------------------------------------------------------------------------
@login_required(login_url='bookdit:vlogin')
def index(request):
    #import pdb; pdb.set_trace()
    context = {
    }
    return render(request, 'bookdit/home/index.html', context)