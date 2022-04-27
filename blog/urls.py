from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.base, name="home"),
    path('create_post/', views.createPost, name="create_post"),
    path('post_detail/<str:pk>/', views.postDetail, name="post_detail"),

    # path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    # path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
]
