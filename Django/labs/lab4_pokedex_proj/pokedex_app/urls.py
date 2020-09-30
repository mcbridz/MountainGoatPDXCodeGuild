from django.urls import path
from . import views

app_name = 'pokedex_app'
urlpatterns = [
    path('', views.home, name='home'),
]
