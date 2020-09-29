from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import url
import requests


def urlshortener(request):
    urls = url.objects.all()
    print(urls)
    context = {
        'title': 'URL Shortener',
        'urls': urls,
    }
    return render(request, 'urlshortener_app/shortener.html', context)


def save(request):
    print(request.POST)
    response = requests.get(request.POST['input_url'])
    if response.status_code == 404:
        print('URL invalid')
    else:
        print(request.POST['input_url'] + ' ' + str(response.status_code))
    new_short = url(long_url=request.POST['input_url'])
    new_short.save()
    return HttpResponseRedirect(reverse('urlshort:urlshortener'))


def redirect(request, code):
    print(request)
    print(code)
    return HttpResponseRedirect(reverse('urlshort:urlshortener'))
