from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_followers',
    )


class Post(models.Model):
    class Meta:
        ordering = ('-created_at',)
    text = models.TextField(max_length=256)
    created_by = models.ForeignKey(
        User, related_name='user_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likers = models.ManyToManyField(
        User, related_name='user_liked_posts')
