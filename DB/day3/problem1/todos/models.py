from django.db import models

# Create your models here.
class Todo(models.Model):
    #author = models.ForeignKey()
    title = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
    