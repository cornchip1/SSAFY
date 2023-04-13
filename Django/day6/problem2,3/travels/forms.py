from django import forms
from .models import travels

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        label = 'Location',
        widget = forms.TextInput(
            attrs ={
                'placeholder':'ex) 제주도',
                'maxlength':10,
            }
        )
    )
    plan = forms.CharField(
        label = 'Plan',
        widget=forms.Textarea(
            attrs = {
                'placeholder':'ex)슉.슈슉.'
            }
        )
    )
    
    start_date = forms.DateField(
        label = 'Start date',
        widget = forms.DateInput(
            attrs = {
                'placeholder':'ex) 2022-02-22'
            }
        )
    )

    end_date = forms.DateField(
        label = 'End date',
        widget = forms.DateInput(
            attrs = {
                'placeholder':'ex) 2022-02-22'
            }
        )
    )


    class Meta:
        model = travels
        fields = '__all__'
