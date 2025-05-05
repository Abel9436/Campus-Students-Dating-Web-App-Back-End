# filepath: c:\Users\binig\Desktop\Dating-app\dating_project\matches\serializers.py
from rest_framework import serializers
from .models import Match  # Import your Match model

class SuggestedMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match  # Replace with the correct model name
        fields = '__all__'  # Adjust fields as needed