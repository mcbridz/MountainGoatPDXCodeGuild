from django.urls import path
from . import views

app_name = 'urlshort'
urlpatterns = [
    path('', views.urlshortener, name='urlshortener'),
    path('save/', views.save, name='save'),
    path('edit/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<str:code>/', views.redirect, name='by_code'),
]
