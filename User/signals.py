from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount

@receiver(post_save, sender=SocialAccount)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.provider == 'google':
        user = instance.user
        # Update user's profile with data from Google
        user.profile_picture = instance.extra_data.get('picture', '')
        user.save()