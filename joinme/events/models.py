import datetime
from django.utils import timezone
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    password = models.CharField(max_length=48)
    email = models.EmailField()
    phone = models.CharField(max_length=24)


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    image = models.FilePathField(path='static/events/images')
    event_location = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateTimeField('event date published')
    publication_date = models.DateTimeField('post date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now
