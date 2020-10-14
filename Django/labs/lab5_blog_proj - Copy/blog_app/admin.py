from django.contrib import admin
from .models import UserProfile, BlogPost

admin.site.register(BlogPost)
admin.site.register(UserProfile)
