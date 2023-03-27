from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','content', 'created_at','updated_at']
    list_display_links = ['id','title']
