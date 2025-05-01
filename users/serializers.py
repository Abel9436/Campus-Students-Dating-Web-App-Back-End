from rest_framework import serializers
from .models import User, UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model dynamically

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Include fields you want to expose

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer to include user details

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'profile_picture']  # Adjust fields as per your model