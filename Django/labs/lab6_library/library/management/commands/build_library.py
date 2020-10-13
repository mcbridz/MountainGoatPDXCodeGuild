from django.core.management.base import BaseCommand
from ...models import Book
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Starting build_library.py')
        with open('./library/management/commands/books.json', 'r', encoding='utf-8') as books:
            print('books.json has been opened')
            book_data = books.read()
            book_data = json.loads(book_data)
            book_data = book_data['books']
            # print(book_data[0])
            # ^ this works
            for book in book_data:
                author = book['author']
                country = book['country']
                image = 'https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/4%20Django/labs/images/' + \
                    book['image']
                language = book['language']
                url = book['url']
                pages = book['pages']
                title = book['title']
                year = book['year']
                new_book = Book(author=author, country=country, image=image,
                                language=language, url=url, pages=pages, title=title, year=year)
                print(f'{new_book.title} SAVED')
                new_book.save()
            print('exiting json')
        print('exiting build_library.py')
