import os
import django
import random
from datetime import date, timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dating_project.settings')
django.setup()

from users.models import User, UserProfile
from matches.models import Match
from chat.models import Message

# Sample data
genders = ['M', 'F', 'O']
locations = ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Dallas']

def create_users(num=5):
    users = []
    for i in range(1, num + 1):
        email = f'user{i}@example.com'
        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': f'user{i}', 'is_verified': True}
        )
        if created:
            user.set_password('password123')
            user.save()
        profile, _ = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'bio': f'This is user{i} bio.',
                'gender': random.choice(genders),
                'birth_date': date.today() - timedelta(days=365*random.randint(18, 30)),
                'location': random.choice(locations),
                'is_verified': True
            }
        )
        users.append(user)
    return users

def create_matches(users):
    for from_user in users:
        to_users = random.sample([u for u in users if u != from_user], k=2)
        for to_user in to_users:
            Match.objects.get_or_create(
                from_user=from_user,
                to_user=to_user,
                defaults={'is_liked': True, 'is_matched': random.choice([True, False])}
            )

def create_messages(users):
    for i in range(5):
        sender, recipient = random.sample(users, 2)
        Message.objects.create(
            sender=sender,
            recipient=recipient,
            content=f'Hello from {sender.username}!',
            timestamp=timezone.now()
        )

if __name__ == '__main__':
    users = create_users()
    create_matches(users)
    create_messages(users)
    print("✅ Database populated with sample users, matches, and messages.")
