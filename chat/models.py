from django.db import models
from account.models import User
from datetime import datetime


class Room(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms', null=True)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messages', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_messages', null=True)
