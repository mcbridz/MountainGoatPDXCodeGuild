from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from .models import Book
from django.shortcuts import get_object_or_404


def search(request):
    print(request.GET)
    parameter = request.GET['parameter']
    # print(parameter)
    search_text = request.GET['text']
    page = request.GET['page']
    if parameter not in ['title', 'author', 'year', 'country', 'language', ]:
        return HttpResponse('Invalid Parameter')
    # book_response = Book.objects.filter(author__icontains=author)
    print('search_text: ' + search_text)
    if search_text == '':
        print('Empty search string')
        book_response = Book.objects.all().order_by('-year')
    else:
        book_response = Book.objects.filter(
            **{parameter+'__icontains': search_text}).order_by('-year')
    print(book_response)
    books_per_page = 5
    paginator = Paginator(book_response, books_per_page)
    page_display = paginator.page(page)
    back_possible = True
    if int(page) == 1:
        back_possible = False
    forward_possible = True
    if int(page) + 1 > paginator.num_pages:
        forward_possible = False
    # print(book_response)
    books = {'books': []}
    for book in page_display:
        books['books'].append({
            'title': book.title,
            'author': book.author,
            'image': book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language,
            'id': book.id,
            'favorited': book.favorited,
        })
    books['paginator_controls'] = {
        'back_possible': back_possible,
        'forward_possible': forward_possible,
        'num_pages': paginator.num_pages
    }
    return JsonResponse(books)
    # return HttpResponse('search complete')
# demo link:
# http://localhost:8000/search/?author=woolf&page=1


def change_favorite(request):
    print(request)
    book = get_object_or_404(Book, id=request.GET['book_id'])
    if book.favorited:
        book.favorited = False
    else:
        book.favorited = True
    book.save()
    return HttpResponse('finished change_favorite view')


def library(request):
    print('library method started')
    library_data = Book.objects.all().order_by('-year')
    library = []
    books_per_page = 5
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
    search_parameters = [
        'title',
        'author',
        'year',
        'country',
        'language',
    ]
    return render(request, 'library/index.html', {'search_parameters': search_parameters})
