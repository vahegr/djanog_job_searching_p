from django.db import models
from account.models import User
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=1000)
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms', null=True)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    room = models.CharField(max_length=1000000)
