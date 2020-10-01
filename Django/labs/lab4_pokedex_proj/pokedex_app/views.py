from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Pokemon


def home(request):
    pokemons = Pokemon.objects.all().order_by('number')
    search_string = ''
    search_type = ''
    if request.GET.get('search_type', False):
        search_type = request.GET['search_type']
        if request.GET['search_type'] == 'name_and_type':
            search_string = request.GET['search_string']
            pokemons = pokemons.filter(
                name__icontains=search_string, types__icontains=search_string)
        elif request.GET['search_type'] == 'name':
            search_string = request.GET['search_string']
            pokemons = pokemons.filter(name__icontains=search_string)
        elif request.GET['search_type'] == 'type':
            search_string = request.GET['search_string']
            pokemons = pokemons.filter(types__icontains=search_string)
    pokemon_per_page = 1
    print(request.GET)
    page_number = request.GET.get('page', 1)
    print(f'Loading page: {page_number}')
    paginator = Paginator(pokemons, pokemon_per_page)
    pokepage = paginator.page(page_number)
    back_ten_number = int(page_number) - 10
    forward_ten_number = int(page_number) + 10
    back_ten_possible = True
    if int(page_number) - 10 <= 0:
        back_ten_possible = False
    forward_ten_possible = True
    if int(page_number) + 10 > paginator.num_pages:
        forward_ten_possible = False
    context = {
        'pokemons': pokepage,
        'paginator': paginator,
        'page_number': page_number,
        'back_ten_possible': back_ten_possible,
        'forward_ten_possible': forward_ten_possible,
        'back_ten_number': back_ten_number,
        'forward_ten_number': forward_ten_number,
        'search_type': search_type,
        'search_string': search_string,
    }
    print(context)
    return render(request, 'pokedex_app/home.html', context)
