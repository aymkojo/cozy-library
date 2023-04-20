from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'baseapp/home.html', {})

def bookPage(request):
    return render(request, 'baseapp/book.html', {})

def signup(request):
    return render(request, 'baseapp/signup.html', {})

def loginPage(request):
    #great work to be done here
    return render(request, 'baseapp/login.html', {})


