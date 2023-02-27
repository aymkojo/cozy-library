from django.urls import path, include
from . import views



urlpatterns = [
    path('home', views.home, name = "home"),
    path('login', views.loginPage, name = "login"),
    path('signup', views.signUp, name = "signup")
]