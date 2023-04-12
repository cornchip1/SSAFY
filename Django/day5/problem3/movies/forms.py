from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = 'title',
        widget = forms.TextInput(
            attrs = {
                'placeholder':'ex) 세얼간이',
                'maxlength' : 50,
            }
        ) 
    )
    
    director = forms.CharField(
        label = 'director',
        widget= forms.TextInput(
            attrs = {
                'placeholder':'ex) 라지쿠마르 히라니',
                'maxlength':30,
            }
        )
    )

    comment = forms.CharField(
        label = 'comment',
        widget= forms.Textarea(
            attrs = {
                'placeholder':'ex) 나 얼간이 아니다!',
                'cols':40,
                'rows':3,
            }
        )
    )
    class Meta:
        model = Movies
        fields = '__all__'