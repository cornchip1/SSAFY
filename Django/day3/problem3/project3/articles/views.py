from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'title':article.title,
        'content': article.content
    }
    return render(request,'articles/index.html', context)
