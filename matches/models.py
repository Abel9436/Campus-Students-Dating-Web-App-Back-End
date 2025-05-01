from django.db import models
from users.models import User

class Match(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_received')
    is_liked = models.BooleanField(default=False)
    is_matched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.email} ➝ {self.to_user.email} | Liked: {self.is_liked} | Matched: {self.is_matched}"
