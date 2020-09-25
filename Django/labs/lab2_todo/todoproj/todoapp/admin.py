from django.contrib import admin
from .models import ToDoItem, Priority

admin.site.register(ToDoItem)
admin.site.register(Priority)
