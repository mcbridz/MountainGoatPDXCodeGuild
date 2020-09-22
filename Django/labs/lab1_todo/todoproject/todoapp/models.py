from django.db import models


class ToDoItem(models.Model):
    topline = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.topline + ':' + self.date_created.strftime("%c")
