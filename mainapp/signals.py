from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages

def show_message_logged_out(sender, user, request, **kwargs):
    messages.warning(request, 'You have been logged out.')

def show_message_logged_in(sender, user, request, **kwargs):
    messages.info(request, 'Welcome back '+user.username)

user_logged_out.connect(show_message_logged_out)
user_logged_in.connect(show_message_logged_in)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()