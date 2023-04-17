from django import forms
from .models import Question, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('pick','content')

class QuestionForm(forms.ModelForm):
    issue_a = forms.CharField(
        label = 'Red TEAM'
    )
    issue_b = forms.CharField(
        label = 'Blue TEAM'
    )
    class Meta:
        model = Question
        fields = '__all__'
