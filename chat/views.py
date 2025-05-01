from rest_framework import generics, permissions
from django.db.models import Q  # Import Q for complex queries
from .models import Message
from .serializers import MessageSerializer

class MessageListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        """
        Return the messages between the authenticated user and another user.
        """
        user = self.request.user
        recipient_username = self.request.query_params.get('recipient')  # Get recipient from query params
        if recipient_username:
            return Message.objects.filter(
                (Q(sender=user) & Q(recipient__username=recipient_username)) |
                (Q(sender__username=recipient_username) & Q(recipient=user))
            ).order_by('timestamp')
        return Message.objects.none()  # Return no messages if no recipient is specified

    def perform_create(self, serializer):
        """
        Add the sender (authenticated user) when creating a message.
        """
        serializer.save(sender=self.request.user)