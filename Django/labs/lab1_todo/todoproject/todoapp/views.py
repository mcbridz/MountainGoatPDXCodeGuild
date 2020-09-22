from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem
from django.urls import reverse
import datetime


def index(request):
    todo_items = ToDoItem.objects.order_by('-date_created')
    context = {
        'todo_items': todo_items,
    }
    for todo_item in todo_items:
        tmp_date = todo_item.date_created
        todo_item.date_created = tmp_date.strftime("%c")
    return render(request, 'todoapp/index.html', context)

# Create your views here.


def save_todo_item(request):
    print(request.POST)
    information = request.POST
    date_created = datetime.datetime.now()
    topline_info = information['input_topline']
    description_info = information['input_description']
    todo = ToDoItem(topline=topline_info,
                    description=description_info, date_created=date_created)
    todo.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
