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

    # 데이터 생성
    article = Article(title=title,content=content)
    article.save()

    return render(request,'articles/create.html')
    #return redirect('articles:index')
    #return redirect('articles:detail',article.pk)