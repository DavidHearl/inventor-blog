""" url paths for post pages """
from django.urls import path
from . import views


urlpatterns = [
    path("create-post/", views.create_post, name="create_post"),
    path("my-posts/", views.UserPosts.as_view(), name="my_published_posts"),
    path("pending-approval/",
         views.PendingPosts.as_view(), name="my_pending_posts"),
    path("pending-approval/<int:pk>",
         views.DraftPostDetail.as_view(), name="draft_post_detail"),
    path("my-posts/<int:pk>update-post/",
         views.UpdatePost.as_view(), name="update_post"),
    path("my-posts/delete-post/<int:pk>",
         views.DeletePost.as_view(), name="delete_post"),
    path("my-posts/<int:pk>/update-pending-posts",
         views.UpdatePendingPost.as_view(), name="update_draft"),
    path("my-posts/delete-pending-post/<int:pk>",
         views.DeletePendingPost.as_view(), name="delete_draft"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>/", views.LikePost.as_view(), name="like_post")
]
