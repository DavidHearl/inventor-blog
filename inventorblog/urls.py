""" Inventorblog urls """
from django.contrib import admin
from django.urls import path, include
from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", views.PostList.as_view(), name="home"),
    path('posts/', include('post.urls'), name='post_urls'),
    path('users/', include('users.urls'), name='user_urls'),
]
