from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='users', blank=True)

    portfolio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,

        )
        profile.save()


