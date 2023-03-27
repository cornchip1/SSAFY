from django.contrib import admin
from .models import Movie

# Register your models here.
class PostMovie(admin.ModelAdmin):
    list_display=['id','title','genre','director']
    list_display_link=['id','title']

admin.site.register(Movie,PostMovie)