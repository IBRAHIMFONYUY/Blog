
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse    
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog

def index(request):
    blogs=Blog.objects.all()
    
    context={
        'blogs':blogs
    }
    return render(request, 'index.html', context)
    

def create(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')  
        password2=request.POST.get('password2')   
        email=request.POST.get('email') 
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already in use')
                return redirect('create')
           
            else:
                user=User.objects.create_user(username=username, password=password, email=email)
                login(request, user)
                messages.success(request, 'account created')
                return redirect('index')
        else:
            messages.error(request, 'password does not match')
            return redirect('create')
        
    return render(request,'signup.html')

def login_user(request):
    page =('login')
    
    if request.user.is_authenticated:
        return redirect('index')
    
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        try:
            user=User.objects.get(username=username)
        except:
            messages.info(request, 'user does not exist')
        
        user=authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login succesfull')
            return redirect('index')

       
            
            
    context={'page':page}
    
    return render(request, 'login.html', context)
def logout_user(reqeust):
    logout(reqeust)
    return redirect('index')  

@login_required(login_url='login')    
def profile(request, pk):
    user=User.objects.get(id=pk)
    blog=user.blog_set.all()
    rooms=Blog.objects.all()
    room_messages=user.message_set.all()
    
    
    context={'user':user, 'db':blog, 'room_messages':room_messages, 'rooms':rooms }
    return render(request, 'profile.html' , context)
 
def blog(request):
    blogs=Blog.objects.all()
    
    context={
        'blogs':blogs
    }
    return render(request, 'blog.html', context)

def single(request, pk):
    blog=Blog.objects.get(id=pk)
    context={
        'blog':blog
    }
    return render(request, 'single.html', context)

@login_required(login_url='login') 
def create_blog(request):
    if request.method == 'POST':
        if request.FILES.get('image') is not None:
            blog=Blog.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('body'),
                user=request.user,
                image=request.FILES.get('image'),
            )
        else:
            blog=Blog.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('body'),
                user=request.user,
            )
        blog.save()
        messages.success(request, 'blog created successfully')
        return redirect('blogs')
    return render(request, 'create.html')


@login_required(login_url='login') 
def delete_blog(request, pk):
    if request.user.is_authenticated:   
        blog=Blog.objects.get(id=pk)
        if request.method == 'POST':
            blog.delete()
            messages.success(request, 'blog deleted ')
            return redirect('blogs')
        context={
            'obj':blog
        }
    return render(request, 'delete.html', context)
def update_post(request, pk):
    blog=Blog.objects.get(id=pk)
    if request.method == 'POST':
        
                blog.title=request.POST.get('title'),
                blog.description=request.POST.get('body'),
                blog.user=request.user,
                blog.image=request.FILES.get('image'),
         
            
                blog.save()
                messages.success(request, 'blog created successfully')
                return redirect('blogs')
    return render(request, 'create.html')
        
    
    
    
                
            
