from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('save_post/', views.save_post, name='save_post'),
    path('logout/', views.logout, name='logout'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('post_view/<int:post_id>', views.post_view, name='post_view'),
]
