# from django.test import TestCase, Client
# from .models import Post
# from django.contrib.auth.models import User
# from django.urls import reverse
# import os
# from django.conf import settings
# from django.contrib.auth import get_user_model

import unittest

class TestView(unittest.TestCase):
    
    def test_index_load(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/index.html')


    def test_post_detail_load(self):
        post = Post.objects.create(
        title='Hello', author=self.users[0]['user'])
        url = reverse('post_detail', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/post_detail.html')

    
    def test_user_add_post(self):
        logged_in = self.client.login(
        username=self.users[0]['username'],
        password=self.users[0]['password'])

        self.assertTrue(logged_in)

        response = self.client.post('/create_post/', {
            'title': 'Hello World',
        })

        self.assertEquals(response.status_code, 302)

        posts = Post.objects.filter(title='Hello World')
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, 'Hello World')

    
    def test_user_delete_post(self):
        logged_in = self.client.login(
            username=self.users[0]['username'],
            password=self.users[0]['password'])

        post = Post.objects.create(
            author=self.users[0]['user'])
        url = reverse('post_delete', kwargs={"pk": 1})
        response = self.client.post(url)

        self.assertRedirects(response, '/')

        posts = Post.objects.filter(title='Hello World')
        self.assertEqual(len(posts), 0)

unittest.main()
