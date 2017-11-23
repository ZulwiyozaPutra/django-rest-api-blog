import uuid
from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Model(models.Model):
    identifier = models.CharField(
        max_length=36,
        unique=True,
        primary_key=True,
        default=uuid.uuid4().hex,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        null=False,
    )
    bio = models.TextField(max_length=255, null=False)
    location = models.CharField(max_length=36, null=False)

    class Meta:
        ordering = ('created',)


class Post(Model):
    owner = models.ForeignKey(
        to='Profile',
        related_name='posts',
        on_delete=models.CASCADE,
        null=False,
    )
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=1000, null=False)


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        # print(sender + kwargs)
