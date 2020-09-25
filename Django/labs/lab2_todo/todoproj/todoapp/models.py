from django.db import models


class Priority(models.Model):
    priority_text = models.CharField(max_length=10)

    def __str__(self):
        return self.priority_text


class ToDoItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)

    def __str__(self):
        return self.description + ' ' + str(self.created_date)
