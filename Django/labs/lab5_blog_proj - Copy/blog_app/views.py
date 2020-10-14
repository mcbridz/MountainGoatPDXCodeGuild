from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile, BlogPost, Comment
import requests
import random


# from django.contrib.auth import login as login_user
import django.contrib.auth


def welcome(request):
    return HttpResponse('Hello, World!')


def index(request):
    return HttpResponseRedirect(reverse('blog_app:login'))


def home(request):
    feed = BlogPost.objects.all().order_by('-date_created')
    authenticated = False
    if request.user.is_authenticated:
        authenticated = True
    return render(request, 'blog_app/home.html', {'feed': feed, 'authenticated': authenticated})


@login_required
def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('blog_app:login'))


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if post.user != request.user:
        return HttpResponseRedirect(reverse('blog_app:home'))
    context = {
        'title': post.title,
        'body': post.body,
        'image': post.image.url,
        'date': post.date_created,
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', context)


def post_view(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    context = {
        'title': post.title,
        'body': post.body,
        'image': post.image.url,
        'date': post.date_created,
        'post': post,
        'authenticated': False,
    }
    if request.user.is_authenticated:
        context['authenticated'] = True
    return render(request, 'blog_app/post_view.html', context)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('blog_app:profile'))


@login_required
def save_post(request):
    blog_data = request.POST
    # print(blog_data)
    title = blog_data['title']
    body = blog_data['body']
    blog_post = BlogPost(title=title, body=body, user=request.user)
    if request.FILES.get('image', False):
        image = request.FILES['image']
        blog_post.image = image
    blog_post.save()
    print(blog_post.id)
    return HttpResponseRedirect(reverse('blog_app:post_detail', args=[blog_post.id]))


@login_required
def profile(request):
    posts = BlogPost.objects.filter(
        user=request.user).order_by('-date_created')
    print(posts)
    context = {
        'user': request.user,
        'posts': posts,
    }
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        image = request.FILES['profile_picture']
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        user.first_name = first_name
        user.last_name = last_name
        user.profile.profile_picture = image
        user.profile.save()
        user.save()
    return render(request, 'blog_app/profile.html', context)


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
        return HttpResponseRedirect(reverse('blog_app:profile'))
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
        ################################################
        # need captcha logic
        ################################################
        # user login logic here
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(
            request, username=username, password=password)
        if user is None:
            message = 'not_found'
        else:
            django.contrib.auth.login(request, user)
            next = request.GET.get('next', reverse('blog_app:home'))
            return HttpResponseRedirect(next)
    context = {
        'site_key': settings.RECAPTCHA_SITE_KEY
    }
    if request.method == 'POST' and not result_json.get('success'):
        context['is_robot'] = True
    return render(request, 'blog_app/login.html', context)
