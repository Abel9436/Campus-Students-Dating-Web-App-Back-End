# filepath: c:\Users\binig\Desktop\Dating-app\dating_project\matches\views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .services import suggest_matches_for
from .serializers import SuggestedMatchSerializer

class SuggestMatchListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SuggestedMatchSerializer

    def get(self, request, *args, **kwargs):
        suggestions = suggest_matches_for(request.user)
        serializer = self.get_serializer(suggestions, many=True)
        return Response(serializer.data)