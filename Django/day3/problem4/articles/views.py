from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context ={
        #'movie':movie,
        'title': movie.title,
        'genre': movie.genre,
        'director':movie.director,
    }
    
    return render(request,'articles/index.html',context)