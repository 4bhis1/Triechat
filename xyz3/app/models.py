from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)


class Message(models.Model):
    room = models.CharField(max_length=100, blank=False)
    user = models.CharField(max_length=100, blank=False)
    msg = models.CharField(max_length=100000, blank=True)
    file = models.FileField(upload_to='',
                            max_length=1000, blank=True)
    time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
