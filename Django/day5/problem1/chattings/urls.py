from django.urls import path
from . import views

app_name = 'chattings'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>/',views.detail,name='detail'),
    path('create/',views.create,name='create'),
    # path('<int:pk>/edit/',views.edit,name='edit'),
    # path('<int:pk>/delete',views.delete,name='delete')
]
