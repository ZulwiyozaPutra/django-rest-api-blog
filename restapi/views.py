from .models import Profile, Post
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProfileSerializer, Post
from rest_framework import generics


class CreateUserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreatePostListView(generics.ListCreateAPIView):
    pass

