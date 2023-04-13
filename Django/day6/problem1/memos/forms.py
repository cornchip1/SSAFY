from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label = 'summary',
        widget= forms.TextInput(
            attrs = {
                'maxlength':20,
                'placeholder' : 'summary'
            }
        )
    )
    memo = forms.CharField(
        label = 'memo',
        widget=forms.Textarea(
            attrs = {
                'placeholder':'memo',
                'cols':50,
                'rows':5,
            }
        )
    )
    
    class Meta:
        model = Memo 
        fields = '__all__'
