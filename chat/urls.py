from django.urls import path
from .views import MessageListView, NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message-list-create'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/mark-read/', MarkNotificationAsReadView.as_view(), name='mark-notification-read'),
]