from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Pokemon, PokemonType
from django.urls import reverse
import random


def home(request):
    print(request)
    poketypes = PokemonType.objects.all().order_by('name')
    pokemons = Pokemon.objects.all().order_by('number')
    search_string = ''
    search_type = ''
    page_number = request.GET.get('page', 1)
    print(f'Loading page: {page_number}')
    pokemon_per_page = 1
    paginator = Paginator(pokemons, pokemon_per_page)
    message = ''
    if request.GET.get('search_type', False):
        search_type = request.GET['search_type']
        if search_type == 'name':
            search_string = request.GET['search_string']
            pokemons = pokemons.filter(name__icontains=search_string).exists()
            print('*************************')
            print(pokemons)
            print('*************************')
            if not pokemons:
                message = "No pokemon matching " + request.GET['search_string']
                pokemons = Pokemon.objects.all().order_by('number')
                # return HttpResponseRedirect(reverse('pokedex_app:home'))
            else:
                pokemons = Pokemon.objects.all().filter(name__icontains=search_string)
            paginator = Paginator(pokemons, pokemon_per_page)
        elif search_type == 'type':
            search_string = request.GET['search_string']
            pokemons = pokemons.filter(types__name__icontains=search_string)
            paginator = Paginator(pokemons, pokemon_per_page)
        elif search_type == 'random':
            pokemons = Pokemon.objects.all().order_by('number')
            page_number = random.randint(1, paginator.num_pages)
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
        'poketypes': poketypes,
        'paginator': paginator,
        'page_number': page_number,
        'back_ten_possible': back_ten_possible,
        'forward_ten_possible': forward_ten_possible,
        'back_ten_number': back_ten_number,
        'forward_ten_number': forward_ten_number,
        'search_type': search_type,
        'search_string': search_string,
        'message': message,
    }
    print(context)
    return render(request, 'pokedex_app/home.html', context)
