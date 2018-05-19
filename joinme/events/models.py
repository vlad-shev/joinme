from django.db import models
import accounts.models as AccountModels


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    image = models.FilePathField(path='static/events/images')
    event_location = models.CharField(max_length=128)
    account = models.ForeignKey(AccountModels.Account, on_delete=models.CASCADE)
    event_date = models.DateTimeField('event date published')
    publication_date = models.DateTimeField('post date published')

    def __str__(self):
        return 'Post({}* {})'.format(self.id, self.title)
