from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    # 입력한 데이터 가져오기
    title = request.GET.get('title') 
    content = request.GET.get('content')
    created_at = request.GET.get('created_at')
    updated_at = request.GET.get('updated_at')

    # 데이터 생성
    article = Article(title=title,content=content,created_at =created_at,updated_at=updated_at)
    article.save()

    #return render(request,'articles/create.html')
    return redirect('articles:index')
    #return redirect('articles:detail',article.pk)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request,'articles/edut.html',context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail',article.pk)