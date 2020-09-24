from django.db import models


class ToDoItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, black=True)

    def __str__(self):
        return self.description + ' ' + str(self.completed_date)
