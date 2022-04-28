from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm


def logout(request):
    logout(request)
    return redirect('home')


def login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, "Username or Password Incorrect")

        context = {'page': page}
        return render(request, 'views/login_register.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "The registration was not successful")

    context = {'form': form}
    return render(request, 'views/login_register.html')


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'views/index.html', context)


@login_required(login_url='login')
def createPost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        context = {'posts': post}

        if form.is_valid():
            form.save()
            return redirect('base')

    return render(request, 'views/create_post.html', context)


def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    context = {
        'posts': post,
        'comments': comments
    }

    return render(request, 'views/post_detail.html', context)


@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        return redirect('home')

    context = {
        'posts': post
    }
    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'views/delete_post.html', context)
