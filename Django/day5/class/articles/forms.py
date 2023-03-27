from django.forms import ModelForm, Form
from .models import Article

class ArticleForm(ModelForm):
    
    class Meta :
        model = Article
        fields = {'title','content'}