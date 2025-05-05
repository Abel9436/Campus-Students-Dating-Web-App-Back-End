from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()  # Get the custom user model dynamically

class UserCreateView(generics.CreateAPIView):
    """
    API view to create a new user.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class UserListView(generics.ListAPIView):
    """
    API view to list all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileCreateView(generics.CreateAPIView):
    """
    API view to create a new user profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class UserProfileListView(generics.ListAPIView):
    """
    API view to list all user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]