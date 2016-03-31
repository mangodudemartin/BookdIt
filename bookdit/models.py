from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Users - Extends the Django User class with additional information
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #join to the Django model
    vendor = models.ForeignKey('vendor', related_name='user2vendor', default=None, null=True, blank=True)

    
# Vendors - Handles vendor information
class vendor(models.Model):
    name = models.CharField(max_length=255, default='__default')
    description = models.CharField(max_length=4000, default='__default')
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


# Services - Handles Services that Vendors offer
class service(models.Model):
    name = models.CharField(max_length=255, default='__default')
    description = models.CharField(max_length=4000, default='__default')
    supplier = models.ForeignKey(User)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

# Appointments - Handles the scheduling of appointments for Services
class appointment(models.Model):
    timestart = models.DateTimeField(default=timezone.now())
    timeend = models.DateTimeField(default=timezone.now())
    service = models.ForeignKey('service', related_name='appointment2service')
    supplier = models.ForeignKey(User, related_name='appointment2user_supplier')
    customer = models.ForeignKey(User, related_name='appointment2user_customer')
    
    def __str__(self):
        return self.timestart
    

# Schedules - Handles the Supplier's scheduled working times
class schedule(models.Model):
    dayofweek = models.IntegerField(default=1)
    timestart = models.DateTimeField(default=timezone.now())
    timeend = models.DateTimeField(default=timezone.now())
    available = models.BooleanField(default=True)
    supplier = models.ForeignKey(User, related_name='schedule2user')