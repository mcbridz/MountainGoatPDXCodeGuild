from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('library/', views.library, name='library'),
    path('', views.index, name='index'),
]
