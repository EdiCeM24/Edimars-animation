from django.shortcuts import render, redirect
from django.contrib.auth.models import models, auth


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def blog(request):
    return render(request, 'home/blog.html')


def contact(request):
    return render(request, 'home/contact.html')


def projects(request):
    return render(request, 'home/projects.html')


def signup(request):
    return render(request, 'home/signup.html')


def login(request):
    return render(request, 'home/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

