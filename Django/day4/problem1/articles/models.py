from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content=models.TextField()

    def __str__(self):
        return f'{self.id}번재 글 - {self.title}'