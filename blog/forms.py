""" Forms.py used to add the post form """
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """ Add and update the post form """
    class Meta:
        """ Metadata for the add post form"""
        model = Post
        fields = (
            'title',
            'body',
            )

