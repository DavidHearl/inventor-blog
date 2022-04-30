from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import UpdateView, DeleteView
from django.views import generic, View
from django.utils.text import slugify
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    """View for the list of blogs posted by all users"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(View):
    """View post details"""

    def get(self, request, slug, *args, **kwargs):
        """Function to get the post details"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        post.body = post.body.replace(
            "['", '').replace("']", '').replace(
                "]", '').replace(" '", '').split("',")

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "liked": liked
            },
        )


class DraftPostDetail(View):
    """View the post details for posts that are awaiting approval"""
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, slug, *args, **kwargs):
        """Function to grab the post details"""
        queryset = Post.objects.filter(status=0)
        post = get_object_or_404(queryset, slug=slug)

        post.body = post.body.replace(
            '[', '').replace(']', '').replace("'", '').split(',')

        return render(
            request,
            "draft_post.html",
            {
                "post": post,
            },
        )


class LikePost(View):
    """View for the like post function"""

    def post(self, request, slug, *args, **kwargs):
        """
        Like function, displays a like depending on wether the
        user has liked or not liked a post.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def create_post(request):
    """fuction to allow to user to create their own post"""
    post_form = PostForm()

    if request.method == 'POST':
        model = Post()
        results = Post.objects.filter(
            author=request.user, title=request.POST.get('title'))
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():

            if results.count() > 0:
                messages.error(request, 'Duplicate Title!')
                return render(request, "create_post.html",
                              {
                                  "post_form": PostForm(),
                              },
                              )
            else:
                post = post_form.save(commit=False)
                post.body = request.POST.getlist('body')
                post.author = request.user
                post.slug = slugify('-'.join([post.title,
                                                str(post.author)]),
                                      allow_unicode=False)
                messages.success(
                    request, "Post submitted and waiting approval!")
                post.save()
                return redirect('home')
        else:
            messages.error(request, 'Please do not leave any of the required fields blank')
            return render(request, "create_post.html",
                          {
                              "post_form": post_form,
                          },
                          )
    else:
        return render(request, "create_post.html",
                      {
                          "post_form": post_form,
                      },
                      )


class UserPosts(generic.ListView):
    """View for the lists of posts created by the user"""
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'my_posts.html'
    paginate_by = 8


class PendingPosts(generic.ListView):
    """View the list of posts that are pending approval"""
    model = Post
    paginate_by = 8
    queryset = Post.objects.filter(status=0)
    template_name = 'my_drafts.html'


class UpdatePost(UpdateView):
    """View to update posts that have been published"""
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('my_published_posts')

    def form_valid(self, form):
        request = self.request
        messages.success(self.request, 'Post updated successfully!')
        post = form.save(commit=False)
        post.body = request.POST.getlist('body')
        post.author = request.user
        post.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class DeletePost(DeleteView):
    """View to delete published posts"""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('my_published_posts')

    success_message = "Post permanently deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)

    
class UpdatePendingPost(UpdateView):
    """View to update pending posts"""
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('my_pending_posts')

    def form_valid(self, form):
        request = self.request
        messages.success(self.request, 'Post updated successfully!')
        post = form.save(commit=False)
        post.body = request.POST.getlist('body')
        post.author = request.user
        post.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, 'Post cannot be updated, please try again')
        return self.render_to_response(self.get_context_data(form=form))


class DeletePendingPost(DeleteView):
    """View to delete posts that are pending approval"""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('my_pending_posts')

    # Used Stack Overflow to help get this message showing
    success_message = "Post has been permanently deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePendingPost, self).delete(
            request, *args, **kwargs)
