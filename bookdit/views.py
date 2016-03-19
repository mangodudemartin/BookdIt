from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    vendor_list = Vendor.objects.all()
    context = {
               'vendor_list' : vendor_list
               }
    return render(request, 'bookdit/index.html', context)