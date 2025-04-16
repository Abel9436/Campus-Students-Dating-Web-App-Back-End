from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    faculty = models.CharField(max_length=100, blank=True)
    campus = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
