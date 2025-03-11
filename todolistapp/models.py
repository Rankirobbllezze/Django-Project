from django.db import models

# Create your models here.
class Task(models.Model):
    #attributes
    title = models.CharField(max_length=255,unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.title


