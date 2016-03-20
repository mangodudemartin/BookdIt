from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    if request.user.is_authenticated():
        context = {
            'current_username': user.username
        }
    else :
        contect = {
            'current_username': ''
        }
    return render(request, 'bookdit/index.html', context)
