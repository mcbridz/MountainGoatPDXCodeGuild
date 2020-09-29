from django.db import models
import random


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


class url(models.Model):
    long_url = models.CharField(max_length=500)
    short_url = make_short()
    counter = 0

    def __str__(self):
        return self.long_url + ' ' + self.short_url
