from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """
    This view is used when a visitor wants to register
    an account on the website.
    """
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            message.success(request, 'User account created successfully')
            return redirect('home')
        else:
            messages.error(request, "The registration was not successful")

    context = {'form': form}
    return render(request, 'views/register.html')


def index(request):
    """
    This view is the main view found when
    entering the website, it displays a list of posts.
    """
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'views/index.html', context)


def postDetail(request, pk):
    """
    View that displays each individual post
    """
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all().order_by('-created')

    liked = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True
        try:
            if request.POST.get('body') == '':
                messages.error(
                    request, "This field has been left blank"
                )
            else:
                comment = Comment.objects.create(
                    author=request.user,
                    post=post,
                    body=request.POST.get('body')
                )
            message.success(
                request, "Your comment has been posted sucessfully"
            )
        except Exception as E:
            print(E)
            return redirect('post_detail', pk=post.id)
        return redirect('post_detail', pk=post.id)

    context = {
        'posts': post,
        'comments': comments,
        'liked': liked
    }
    return render(request, 'views/post_detail.html', context)


def likePost(request, pk):
    """
    Function that controls the adding and subtracting of likes
    """
    post = Post.objects.get(id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


@login_required(login_url='login')
def createPost(request):
    """
    This view (for users who have logged in) allows
    users to create posts
    """
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post was created successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'views/create_post.html', context)


@login_required(login_url='login')
def deletePost(request, pk):
    """
    This view (for users who have logged in) allows
    users to delete thier own posts
    """
    text_type = 'post'
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return redirect('home')

    if request.user != post.author:
        return redirect('home')

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Your post has been deleted sucessfully')
        return redirect('home')

    context = {
        'posts': post,
        'text_type': text_type
    }

    return render(request, 'views/delete.html', context)


@login_required(login_url='login')
def deleteComment(request, pk):
    """
    This view (for users who have logged in) allows
    users to delete thier own comments
    """
    post_id = request.GET.get('post_id')
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return redirect('post_detail', pk=post_id)

    if request.user != comment.author:
        return redirect('home')

    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Your comment was sucessfully deleted')
        return redirect('post_detail', pk=post_id)

    context = {'comment': comment, 'post_id': post_id}
    return render(request, 'views/delete.html', context)
