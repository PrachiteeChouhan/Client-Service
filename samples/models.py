from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Service_Provider(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    service_name=models.CharField(max_length=200, default='')
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        """return the name of the service provider"""
        return self.service_name
    
    
        
class Client(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=200, default='')
    
    def __str__(self):
        """return the name of the client"""
        return self.text

    