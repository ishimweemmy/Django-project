from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('view_post/<str:pk>', views.view_post, name='view_post'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
