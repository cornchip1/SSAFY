from django.contrib import admin
from .models import Article


# Register your models here.
class PostAdmin(admin.ModelAdmin) :
    list_display=['pk','title','content','created_at','updated_at']
    list_display_links=['pk','title']

admin.site.register(Article, PostAdmin)