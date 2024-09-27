from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import TimeStampedModel


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(blank=True)


class Follow(TimeStampedModel):
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_user')
    receive_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_user')

    class Meta:
        unique_together = ('send_user', 'receive_user')