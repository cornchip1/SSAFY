from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'articles/index.html',context)

def detail(request,pk):
    article = Article.objects.get(id=pk)
    context = {'article':article}
    return render(request,'articles/detail.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # # DB에 새로운 article 저장
    # Article.objects.create(
    #     title = title,
    #     content = content
    # )

    article = Article(title = title, content = content)
    # 새로운 로직 추가
    article.save()

    # 새로운 url 로 리디렉션
    return redirect('articles:index')

