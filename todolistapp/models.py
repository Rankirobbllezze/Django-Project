from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

#create a custom user model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    def __str__(self):
        return self.username









# Create your models here.
class Taskers(models.Model):
    """custom class to list our taskers"""
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Task(models.Model):
    #attributes
    title = models.CharField(max_length=255,unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # here establishing a one to many relationship using a FK
    tasker = models.ForeignKey(Taskers, on_delete=models.SET_NULL, null=True, blank=True)


    # this tags the user who creates the task
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

def __str__(self):
        return self.title

"""
1. python3 manage.py migrate todolistapp zero
2. python3 manage.py makemigrations appname
3. python3 manage.py migrate
"""




