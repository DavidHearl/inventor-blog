from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostForm
from .models import Post, Comment


def logout(request):
    logout(request)
    return redirect('home')


def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, "Username or Password Incorrect")

        context = {}
        return render(request, 'views/login.html', context)


def index(request):
    posts = Post.objects.all()
    context = {'post': posts}

    return render(request, 'views/index.html', context)



@login_required(login_url='login')
def createPost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        context = {'post': post}

        if form.is_valid():
            form.save()
            return redirect('base')

    return render(request, 'views/create_post.html', context)


def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    
    return render(request, 'views/post_detail.html', context)


def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'views/delete_post.html', context)


# from django.views import generic, View
# from .models import Post
# from .forms import CommentForm


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 6


# class PostDetail(View):
#     """
#     Gets the post detail view
#     """

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm(),
#             },
#         )

#     def post(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         comment_form = CommentForm(data=request.POST)

#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
#         else:
#             comment_form = CommentForm()

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": True,
#                 "liked": liked,
#                 "comment_form": CommentForm(),
#             },
#         )


# class PostLike(View):
#     def post(self, request, slug, *args, **kwargs):
#         post = get_object_or_404(Post, slug=slug)
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)

#         return HttpResponseRedirect(reverse("post_detail", args=[slug]))
