from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=40)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=500)
    image_back = models.CharField(max_length=500)
    types = models.ManyToManyField(
        PokemonType, related_name='pokemons')

    def __str__(self):
        return self.name + ' ' + str(self.number)
