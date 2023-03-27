from django.urls import path
from . import views

app_name = 'calculators'
urlpatterns = [
    path('calculator/<int:n1>/<int:n2>',views.calculator,name='calculator'),    
]