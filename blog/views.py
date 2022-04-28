from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
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

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')

    return render(request, 'views/create_post.html', context)


def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all().order_by('-created')

    liked = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True
        comment = Comment.objects.create(
            author=request.user,
            post=post,
            body=request.POST.get('body')
        )
        return redirect('post_view', pk=post.id)

    context = {
        'posts': post,
        'comments': comments,
        'liked': liked
    }

    return render(request, 'views/post_detail.html', context)


def likePost(request, pk):
    post = Post.objects.get(id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


@login_required(login_url='login')
def deletePost(request, pk):
    text_type = 'post'
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        return redirect('home')

    context = {
        'posts': post,
        'text_type': text_type
    }
    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'views/delete_post.html', context)


@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    post_id = request.GET.get('post_id')
    print(post_id)

    if request.user != comment.author:
        return redirect('home')

    if request.method == "POST":
        comment.delete()
        return redirect('post_detail', pk=post_id)

    context = {'comment': comment, 'post_id': post_id}
    return render(request, 'views/delete_post.html', context)
