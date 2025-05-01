from django.urls import path
from .views import (
    UserCreateView,
    UserListView,
    UserProfileCreateView,
    UserProfileListView,
)

urlpatterns = [
    # User-related endpoints
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),

    # UserProfile-related endpoints
    path('profiles/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profiles/', UserProfileListView.as_view(), name='profile-list'),
]