from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
