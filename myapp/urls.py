from django.urls import path
from . import views

urlpatterns = [
    path('' , views.post_list , name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('users/' , views.get_user , name='get_user'),
    path('users/<int:pk>/' , views.user_detail, name='user_detail'),
    path('users/add' , views.add_user, name='add_user'),
]