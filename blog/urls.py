from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("", views.index, name="home"),
    path('create_post/', views.createPost, name="create_post"),
    path('post_detail/<str:pk>/', views.postDetail, name="post_detail"),
    path('delete_post/<str:pk>/', views.deletePost, name="delete_Post"),
    path('delete_comment/<str:pk>/', views.deleteComment, name="delete_Comment"),
]
