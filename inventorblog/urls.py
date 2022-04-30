""" Inventorblog urls """
from django.contrib import admin
from django.urls import path, include
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.PostList.as_view(), name="home"),
    path('blog/', include('blog.urls'), name='blog_urls'),
    path('users/', include('users.urls'), name='user_urls'),
]
