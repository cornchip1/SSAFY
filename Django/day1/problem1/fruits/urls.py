from django.urls import path,include
from . import views

app_name = 'fruits'
urlpatterns = [
    path('',views.fruit)
]