from django.db import models
import random


class ShortenedURL(models.Model):
    url = models.CharField(max_length=500)
    code = models.CharField(max_length=10)
    counter = models.IntegerField()

    def __str__(self):
        return self.url + ' ' + self.code
