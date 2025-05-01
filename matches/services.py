from users.models import UserProfile

def suggest_matches_for(user):
    """
    Suggest random profiles to the user based on gender preference.
    Currently returns 10 random users with the same gender as user's preference.
    You can expand this to include interests, distance, etc.
    """
    if not hasattr(user, 'profile'):
        return UserProfile.objects.none()

    return UserProfile.objects.exclude(user=user).filter(
        gender=user.profile.gender
    ).order_by('?')[:10]
