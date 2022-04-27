from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.base, name="home"),
    path('create_post/', views.create_post, name="create_post")

    # path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    # path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
]
