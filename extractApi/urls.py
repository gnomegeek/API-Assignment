from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load, name='load'),
    path('dump/', views.dump, name='dump'),
    path('users/', views.deleteUser, name='users'),
    path('user/info/', views.userInfo, name='usersInfo'),
    path('register/', views.register, name='register'),
]

