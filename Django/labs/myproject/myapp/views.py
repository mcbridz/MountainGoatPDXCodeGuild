# from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel


def index(request):
    # return HttpResponse('hello world!')

    # context = {
    #     'message': 'Hello World!',
    # }
    # return render(request, 'myapp/index.html', context)

    blog_posts = MyModel.objects.order_by('-date_published')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'myapp/index.html', context)
