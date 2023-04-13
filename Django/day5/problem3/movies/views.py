from django.shortcuts import render,redirect
from .models import Movies
from .forms import MovieForm
from django.http import Http404
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    movies = Movies.objects.all()
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    context = {'form':form}
    return render(request,'movies/create.html',context)

@require_http_methods(['GET'])
def detail(request,pk):
    try:
        movie = Movies.objects.get(pk=pk)
        context = {'movie':movie}
    except Movies.DoesNotExist :
        raise Http404('없어용')
    return render(request,'movies/detail.html',context)
