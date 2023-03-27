from django.urls import path,include
from . import views

app_name = 'calculators'
urlpatterns = [
    path('',views.calculation,name='calculation'),
    path('result/',views.result,name='result')
]
