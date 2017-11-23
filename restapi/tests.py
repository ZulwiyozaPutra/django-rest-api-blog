from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Post


class ModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='nerd',
            email='nerd@asfuck.com',
            password='iamnerd',
        )

        self.profile = Profile(
            user=self.user,
            bio='I\'m nerd as fuck',
            location='Nerdberg',
        )

        self.post = Post(
            title='This is the title',
            content='This is the content',
            owner=self.profile
        )

    def test_model_can_create_profile(self):
        old_count = Profile.objects.count()
        self.profile.save()
        new_count = Profile.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)


class SerializerTestCase(TestCase):

    def setUp(self):
        pass
