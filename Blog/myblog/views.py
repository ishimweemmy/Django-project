from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'authenticate/index.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'authenticate/posts.html', {'posts': posts})

def view_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'authenticate/view_post.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        p_number = request.POST['p_number']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        c_password = request.POST['c_password']
        
        credentials = [email, password, firstname, lastname, username, c_password, p_number]
        for credential in credentials:
            if credential == '':
                messages.info(request, f'Please fill out your {credential}')
                return redirect('signup')
            else:
                if password == c_password:
                    if User.objects.filter(username=username).exists() & User.objects.filter(email=email).exists():
                        messages.info(request, 'User already exists')
                        return redirect('signup')
                    elif User.objects.filter(username=username).exists():
                        messages.info(request, 'username already taken')
                        return redirect('signup')
                    elif User.objects.filter(email=email).exists():
                        messages.info(request, 'It seems as if this email is already taken')
                        return redirect('signup')
                    else:
                        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                        user.save();
                        return redirect('posts')
                else:
                    messages.info(request, 'passwords do not match')
                    return redirect('signup')
    else:
        return render(request, 'authenticate/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        credentials = [username, email, password]

        for credential in credentials:
            if credential == '':
                messages.info(request, f'please fill in {credential}')
                return redirect('login')
            else:
                user = auth.authenticate(request, username=username, email=email, password=password)
                
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'Invalid credentials')
                    return redirect('login')
    else:
        return render(request, 'authenticate/login.html')
