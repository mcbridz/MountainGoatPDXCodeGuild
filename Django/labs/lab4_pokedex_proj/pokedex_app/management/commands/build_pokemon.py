import requests
import json
import pyperclip
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = {'pokemon': []}
        num_pokemon = 896
        for i in range(1, num_pokemon):
            # get the data from the pokemon api
            response = requests.get(
                'https://pokeapi.co/api/v2/pokemon/' + str(i))
            if response.status_code == 200:
                pokeapi_data = json.loads(response.text)

                # extract the relevant portions of data
                number = pokeapi_data['id']
                name = pokeapi_data['name']
                height = pokeapi_data['height']
                weight = pokeapi_data['weight']
                image_front = pokeapi_data['sprites']['front_default']
                image_back = pokeapi_data['sprites']['back_default']
                url = 'https://pokemon.fandom.com/wiki/' + name
                types = [type['type']['name']
                         for type in pokeapi_data['types']]

                # put the relevant data into a dictionary
                pokemon = {
                    'number': number,
                    'name': name,
                    'height': height,
                    'weight': weight,
                    'image_front': image_front,
                    'image_back': image_back,
                    'types': types,
                    'url': url
                }

                # add the pokemon to our list
                data['pokemon'].append(pokemon)

                # give the user some feedback
                print(str(round(i / num_pokemon * 100, 2)) + '%')
                print(pokemon['name'])

        # copy the resulting json to the clipboard
        # pyperclip.copy(json.dumps(data, indent=4))
        data = json.dumps(data, indent=4)
        with open('pokemon.json', 'w', encoding='utf-8') as pokedex:
            print('pokemon.json has been opened')
            pokedex.write(data)

        print('pokemon.josn has been closed')
