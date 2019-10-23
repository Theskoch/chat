from django.conf import settings
from django.db import models
from django.utils import timezone


class masege(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hash = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    fazer = models.CharField(max_length=200)
    name_chats = models.CharField(max_length=200)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.hash


class chats(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_chats = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.hash