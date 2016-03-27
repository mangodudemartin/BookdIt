from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(vendor)
admin.site.register(userextend)
admin.site.register(service)
admin.site.register(appointment)
