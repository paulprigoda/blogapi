from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #create user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        #create blogpost
        testpost = Post.objects.create(author=testuser1, title='scruffy tha dawg', body='scruff scruff in the buff buff')
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'scruffy tha dawg')
        self.assertEqual(body, 'scruff scruff in the buff buff')