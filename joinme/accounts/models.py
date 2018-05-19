from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=24)
    link1 = models.URLField()
    link2 = models.URLField()
    link3 = models.URLField()
