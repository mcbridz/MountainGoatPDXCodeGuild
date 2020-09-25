from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('check/<int:todo_item_id>/', views.check_mark, name='check'),
    path('remove_item/<int:todo_item_id>/', views.remove_item, name='kill')
]
