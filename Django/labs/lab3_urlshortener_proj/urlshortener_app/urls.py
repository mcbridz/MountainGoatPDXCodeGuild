from django.urls import path
from . import views

app_name = 'urlshort'
urlpatterns = [
    path('', views.urlshortener, name='urlshortener'),
    path('save/', views.save, name='save'),
    path('<str:code>/', views.redirect, name='by_code')
]
