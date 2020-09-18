from django.db import models

# Create your models here.


class MyModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title + '-' + self.author
