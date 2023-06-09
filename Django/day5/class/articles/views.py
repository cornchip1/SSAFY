from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


from .forms import ArticleForm
def create(request):
    # if request.method == 'GET':
    #     form = ArticleForm()
    #     context = {
    #         'form':form
    #     }
    #     return render(request,'articles/create.html',context)
    # elif request.method == "POST":
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         article = form.save()
    #         return redirect('articles:detail',pk=article.pk)
    #     else: # if is_valid == False, return to previous page with error message
    #         context = {
    #             'form':form 
    #         }
    #         return render(request,'articles/create.html',context)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',pk=article.pk)
    elif request.method == "GET":
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.save()
    #     return redirect('articles:detail', pk=article.pk)
    # else:
    #     return render(request, 'articles/create.html')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    # article = Article.objects.get(pk=pk)
    # if request method == "POST":
    #     form = ArticleForm(request.POST,instance = article)
    #     if form.is_valid():
    #         ~~
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)
