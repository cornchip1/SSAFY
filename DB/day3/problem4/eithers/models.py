from django.db import models

TEAMS = (('Red','Red'),('Blue','Blue'))
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)

class Comment(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    pick = models.CharField(max_length = 9, choices = TEAMS, default = 'Red Team')
    content = models.CharField(max_length=100)