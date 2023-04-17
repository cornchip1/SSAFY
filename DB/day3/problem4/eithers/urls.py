from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('random/',views.random_page,name='random_page'),
    path('<int:question_pk>/',views.detail,name='detail'),
    path('<int:question_pk>/update/',views.update,name='update'),
    path('<int:question_pk>/delete/',views.delete,name='delete'),
    path('<int:question_pk>/comment/',views.comments_create,name='comments_create'),
    path('<int:question_pk>/comment/<int:comment_pk>/delete/',views.comments_delete,name='comments_delete'),
]
