from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import ToDoItem, Priority
from datetime import datetime


def index(request):
    todo_items = ToDoItem.objects.all().order_by('completed_date', '-created_date')
    priorities = get_list_or_404(Priority.objects.all())
    context = {
        'title': 'To-Do List',
        'todo_items': todo_items,
        'priorities': priorities,
    }
    return render(request, 'todoapp/index.html', context)


def save(request):
    print(request.POST)
    date = timezone.now()
    priority = get_object_or_404(Priority, pk=request.POST['priority_id'])
    todo_item = ToDoItem(
        description=request.POST['description'], created_date=date, priority=priority)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def check_mark(request, todo_item_id):
    todo_item = get_object_or_404(ToDoItem, pk=todo_item_id)
    if todo_item.completed_date == None:
        completed_date = timezone.now()
        todo_item.completed_date = completed_date
    else:
        todo_item.completed_date = None
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def remove_item(request, todo_item_id):
    todo_item = get_object_or_404(ToDoItem, pk=todo_item_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))
