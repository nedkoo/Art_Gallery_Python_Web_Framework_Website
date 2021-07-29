from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='users', blank=True)

    portfolio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
