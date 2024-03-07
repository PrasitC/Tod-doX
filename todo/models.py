from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500)
    desc = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(default = timezone.now)
    datecompleted = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False, blank=True, null=True)
   
    date = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    objects = models.Manager()    
    def __str__(self):
        return self.title
    
    
class User(models.Model):
    Name= models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    Password = models.CharField(null= False , blank = False, max_length= 10)
    def __str__(self):
        return self.Name
    