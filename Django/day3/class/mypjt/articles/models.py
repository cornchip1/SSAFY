from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20) # title은 형태, 최대 몇 글자까지 되는지 지정해야함
    content = models.TextField() # 글자 수 없이 저장 가능
    