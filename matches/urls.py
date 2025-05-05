# filepath: c:\Users\binig\Desktop\Dating-app\dating_project\matches\urls.py
from django.urls import path
from .views import SuggestMatchListView

urlpatterns = [
    path('suggestions/', SuggestMatchListView.as_view(), name='suggest-match-list'),
]