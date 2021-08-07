from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from art_gallery_web.gallery_auth.models import UserProfile


def is_negative(value):
    if value <= 0:
        raise ValidationError('The value must be positive')


# Create your models here.
class Arts(models.Model):
    name = models.CharField(max_length=15, blank=False)

    height = models.IntegerField(blank=False, validators=[is_negative, ])
    width = models.IntegerField(blank=False, validators=[is_negative, ])
    price = models.FloatField(blank=False, validators=[is_negative, ])

    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='arts', blank=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.height} / {self.width}'


class Post(models.Model):
    text = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)

    art = models.ForeignKey(Arts, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment {self.text} by {self.name}'

