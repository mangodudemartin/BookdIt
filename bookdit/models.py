from django.db import models

    
#Vendors - Handles vendor information
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    
    def __str__(self):
        return self.name
    

#Users - Handles user's information
class User(models.Model):
    username = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username + "  (" + self.lastName + ", " + self.firstName + ")"
    
