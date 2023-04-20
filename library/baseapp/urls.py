from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('book/', views.bookPage, name='book'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signup/', views.signup, name='signup'),
]
