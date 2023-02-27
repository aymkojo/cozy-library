from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request, 'login.html')


def signUp(request):
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.Post)
    #     if form.is_valid():

        
    return render(request, 'signup.html')
