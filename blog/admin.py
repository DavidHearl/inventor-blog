""" Admin.py used for database setup """ 
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Summernote fields for body text"""
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ('title')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')
