from django.contrib import admin
from django.urls import path
from .views import News, Contact, Home,News_date,register,addUser,addUser1,register2

urlpatterns = [
    path('news/', News, name="news"),
    path('', Home, name="home"),
    path('contact/', Contact, name="contact"),
    path('newsdate/<int:year>', News_date, name="newsdate"),
    path('register/', register, name="register"),
    path('addUser/', addUser, name="addUser"),
    path('addUser1/', addUser1, name="addUser1"),
    path('register1/', register2, name="register1"),



]
