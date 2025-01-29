from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth.models import models, auth, User # type: ignore
from .forms import UserCreationForm, AuthenticationForm, User, SignupForm, LoginForm
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages # type: ignore


@login_required(login_url='login')
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
    form = SignupForm()
    
    if request.method == "POST":
        
        form = SignupForm(request.POST)
        
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
    
            return HttpResponse('Your password is not match! Please sign up with identical password.')
        else:
            messages.success(request, 'You are successfully signed up!')
            
        if form.is_valid():
            
            form.save()
            
            return redirect('login')
    
    context = {'signupForm': form}    
    
    return render(request, 'home/signup.html', context=context)


def login(request):
    form = LoginForm()
    
    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    context = {'loginForm': form}        
    
    return render(request, 'home/login.html', context=context)


def logout(request):
    
    auth.logout(request)
    
    messages.success(request, 'You have been logged out successfully!')
    
    return redirect('login')

