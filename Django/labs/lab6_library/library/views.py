from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Book


def search(request):
    print(request)
    author = request.GET['author']
    # print(request.GET['author'])
    page = request.GET['page']
    # print(request.GET['page'])
    book_response = Book.objects.filter(author__icontains=author)
    print(book_response)
    books = {'books': []}
    for book in book_response:
        books['books'].append({
            'title': book.title,
            'author': book.author,
            'image': book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language,
        })
    return JsonResponse(books)
# demo link:
# http://localhost:8000/search/?author=woolf&page=1


def library(request):
    print('library method started')
    library_data = Book.objects.all().order_by('-year')
    library = []
    for book in library_data:
        library.append({
            'title': book.title,
            'author': book.author,
            'image': book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language,
            'id': book.id,
        })
    return JsonResponse({'library': library})


def index(request):
    return render(request, 'library/index.html')
