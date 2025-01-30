from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth.models import models, auth, User # type: ignore
from .forms import UserCreationForm, AuthenticationForm, User, SignupForm, LoginForm
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages # type: ignore
from django.http import request # type: ignore
from django.core.mail import send_mail # type: ignore
from django.conf import settings # type: ignore
from .models import About, AboutVideo, VideoProject, Project, Home, Blog, BlogVideo



@login_required(login_url='login')
def home(request):
    house = Home.objects.all()
    return render(request, 'home/index.html', {'house': house})


def about(request):
    abouts = About.objects.all()
    about_videos = AboutVideo.objects.all()
    return render(request, 'home/about.html', {
        'abouts': abouts,
        'about_videos': about_videos
    })


def blog(request):
    blogs = Blog.objects.all()
    blog_video = BlogVideo.objects.all()
    
    return render(request, 'home/blog.html', {
        'blogs': blogs,
        'blog_video': blog_video,
    })


def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        uname = request.POST['username']
        message_email = request.POST['message-email']
        subject = request.POST['subject']
        message_text = request.POST['message']
        
        msg_mail = str(message_text) + "\n\nform: " + str(message_email)
        
        send_mail (
            "Contacted By: " + str(message_name),
            msg_mail,
            message_email,
            uname,
            subject,
            [settings.EMAIL_HOST_USER],
            # fail_silently=False
        )
        
        
        return render(request, 'home/contact.html', {
            'message_name': message_name,
            'uname': uname,
            'message_email': message_email,
            'subject': subject,
            'message_text': message_text,
            })
    return render(request, 'home/contact.html', {})    


def projects(request):
    videos = VideoProject.objects.all()
    project = Project.objects.all()
    
    return render(request, 'home/projects.html', {
        'videos': videos,
        'project': project,
        })


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

