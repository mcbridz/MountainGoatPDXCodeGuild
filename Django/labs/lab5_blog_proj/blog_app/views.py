from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile
import requests


# from django.contrib.auth import login as login_user
import django.contrib.auth


def welcome(request):
    return HttpResponse('Hello, World!')


def index(request):
    return HttpResponseRedirect(reverse('blog_app:welcome'))


@login_required
def profile(request):
    user = request.user
    print(user)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'picture': user.profile_picture
    }


def register(request):
    print('GET' + str(request.GET))
    if request.method == 'POST':
        print(request.POST)
        secret_key = settings.RECAPTCHA_SECRET_KEY
        data = {
            'response': request.POST['g-recaptcha-response'],
            'secret': secret_key,
        }
        resp = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result_json = resp.json()
        print(result_json)
        # create user logic here
        password = request.POST['password']
        password_v = request.POST['password_v']
        if password != password_v:
            message = 'passwords do not match'
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            message = 'user already exists'
        user = User.objects.create_user(
            username, request.POST['email'], password)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        django.contrib.auth.login(request, user)
        new_profile = UserProfile(login_name=user)
        new_profile.save()
        HttpResponseRedirect(reverse('blog_app:profile'))
    context = {
        'site_key': settings.RECAPTCHA_SITE_KEY
    }
    return render(request, 'blog_app/registration.html', context)


def login(request):
    print(request.POST)
    print(request.GET)
    if request.method == 'POST':
        secret_key = settings.RECAPTCHA_SECRET_KEY
        data = {
            'response': request.POST['g-recaptcha-response'],
            'secret': secret_key,
        }
        resp = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result_json = resp.json()
        print(result_json)
        # user login logic here
    context = {
        'site_key': settings.RECAPTCHA_SITE_KEY
    }
    if request.method == 'POST' and not result_json.get('success'):
        context['is_robot'] = True
    return render(request, 'blog_app/login.html', context)
