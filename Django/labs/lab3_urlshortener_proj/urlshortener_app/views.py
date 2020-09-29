from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import ShortenedURL
import requests
import random

# Code for figuring out shortened URL


def generateUpper():
    return chr(random.randrange(65, 91))


def generateLower():
    return chr(random.randrange(97, 123))


def generateNum():
    return str(random.randrange(0, 10))


def make_short():
    output = []
    for i in range(6):
        choice = random.choice(['upper', 'lower', 'num'])
        if choice == 'upper':
            output.append(generateUpper())
        elif choice == 'lower':
            output.append(generateLower())
        else:
            output.append(generateNum())
    random.shuffle(output)
    return ''.join(output)
# End Code for figuring out shortened URL


def urlshortener(request):
    urls = ShortenedURL.objects.all()
    # print(urls)
    context = {
        'title': 'URL Shortener',
        'urls': urls,
    }
    return render(request, 'urlshortener_app/shortener.html', context)


def edit(request):
    urls = ShortenedURL.objects.all()
    print(urls)
    context = {
        'title': 'Edit Saved URLs',
        'urls': urls,
    }
    return render(request, 'urlshortener_app/edit.html', context)


def save(request):
    # print(request.POST)
    response = requests.get(request.POST['input_url'])
    if response.status_code == 404:
        print('URL invalid')
    else:
        new_short = ShortenedURL(
            url=request.POST['input_url'], code=make_short(), counter=0)
        new_short.save()
        # print(request.POST['input_url'] + ' ' + str(response.status_code))
    return HttpResponseRedirect(reverse('urlshort:urlshortener'))


def redirect(request, code):
    # print(request)
    # print(code)
    url_object = ShortenedURL.objects.get(code=code)
    url_object.counter += 1
    url_object.save()
    # print('************************************************************')
    # print(url_object)
    # print('************************************************************')
    return HttpResponseRedirect(url_object.url)


def delete(request, id):
    url_object = ShortenedURL.objects.get(pk=id)
    print(url_object)
    url_object.delete()
    return HttpResponseRedirect(reverse('urlshort:edit'))
