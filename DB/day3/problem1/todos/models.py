from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #check_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='check_todos')
    title = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
