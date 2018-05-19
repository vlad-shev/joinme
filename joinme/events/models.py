from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    image = models.FilePathField(path='static/events/images', null=True)
    event_location = models.CharField(max_length=128, null=True)
    #user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    event_date = models.DateTimeField('event date published', null=True)
    publication_date = models.DateTimeField('post date published', auto_now_add=True)

    def __str__(self):
        return 'Post({}* {})'.format(self.id, self.title)



    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= no
