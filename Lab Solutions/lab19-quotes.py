#filename: lab19-quotes.py
#author: Zachary McBride

import requests
import string
import time
import sys

class Quote:
    def __init__(self, data, page, list_of_quotes, last_page):
        self.quote_text = data['body']
        self.quote_author = data['author']
        self.page = page
        self.url = data['url']
        self.last_page = last_page
        list_of_quotes.append(self)
    def get_quote(self):
        return self.quote_text
    def get_author(self):
        return self.quote_author
    def get_url(self):
        return self.url
# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
#pulls list of quotes
# response = requests.get('https://favqs.com/api/quotes?filter=funny', headers = headers)
# print(response.text)
# data = response.json()
# print(data['quotes'][0]['body'])
# print(data['quotes'][0]['author'])
# first_quote = quote(data, 0)
# print(first_quote.get_quote())
# print(first_quote.get_author())
# print(first_quote.get_url())

#how do I want to search?
#by author, by keyword

def insert_string(original, pos, str_insert):
    original_list = [char for char in original]
    original_list.insert(pos, str_insert)
    return ''.join(original_list)

def swap_char(original, value, new_char):
    i_char = original.index(value)
    original_list = [char for char in original]
    original_list[i_char] = new_char
    return ''.join(original_list)


# test_str = 'Hello'
# test_pos = 2
# test_ins = 'ii'

# print(insert_string(test_str, test_pos, test_ins))

# test_dict = {1: 'apple'}
# print(len(test_dict))
# for item in test_dict:
#     print(test_dict[item])


def get_json(str_request, headers):
    response = requests.get(str_request, headers = headers)
    data = response.json()
    return data['quotes'], data['page'], data['last_page']

def split_quotes(new_data, page, list_of_quotes, last_page):
    for quote in new_data:
        temp_quote = Quote(quote, page, list_of_quotes, last_page)

def build_list(list_of_quotes, json_data, str_request, page, header):
    if not list_of_quotes[len(list_of_quotes) - 1].last_page:
        q_index = str_request.index('?') + 1
        new_search = insert_string(str_request, q_index, f'page={str(page)}&')
    else:
        return
    while not list_of_quotes[len(list_of_quotes) - 1].last_page:
        p_index = int(new_search.index(str(page)))
        new_search = swap_char(new_search, str(page), str(page + 1))
        page += 1
        if page == 5:
            break
        new_data, page, last_page = get_json(new_search, header)
        split_quotes(new_data, page, list_of_quotes, last_page)
        time.sleep(5)

def print_quotes(list_of_quotes, page):
    for quote in list_of_quotes:
        if quote.page == page:
            print(quote.quote_text)
            print(quote.quote_author)
            print()
        if quote.last_page == True:
            return False
    return True

def quote_menu(list_of_quotes, keyword, headers):
    page = 1
    max_page = 1
    for quote in list_of_quotes:
        if max_page < quote.page:
            max_page = quote.page
    while True:
        last_page = print_quotes(list_of_quotes, page)
        print(f'Page {page}/{max_page}')
        continue_q = input('Press ENTER to see next page, Z, for previous, R for restart, Q to quit').lower()
        if continue_q not in ['', 'z']:
            break
        elif continue_q == 'z':
            page -= 1
            if page == 0:
                page = 1
        elif continue_q == 'r':
            return True
        elif continue_q == 'q':
            exit()
        else:
            if page == max_page or not last_page:
                page += 1
                new_search = f'https://favqs.com/api/quotes?page={page}filter={keyword}'
                data, page, last_page = get_json(new_search, headers = headers)
                max_page += 1
                split_quotes(data, page, list_of_quotes, last_page)
            elif page < max_page:
                page += 1
            else:
                print('Last page reached.')

def get_random_quote(headers):
    temp_data = requests.get('https://favqs.com/api/qotd', headers = headers)
    data = temp_data.json()
    print(f"""
    {data['quote']['body']}
    {data['quote']['author']}""")
    if input('Press ENTER to continue, type <quit> to quit. ') != '':
        sys.exit()


def main():
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    print('Welcome to the quote search engine, powered by favqs.com/api.')
    collated_data = []
    while True:
        type_query = input(f'How would you like to search? By random sets, or by keyword? (type <quit> to quit)').lower().strip()
        while type_query not in ['r', 'rand', 'random', 'k', 'key', 'keyword', 'q', 'quit', 'exit']:
            type_query = input('Invalid entry, please enter "random" or "keyword" for the type of search you would like to perform. ')
        if type_query in ['r', 'rand', 'random']:
            type_query = 'random'
        elif type_query in ['k', 'key', 'keyword']:
            type_query = 'keyword'
        elif type_query in ['q', 'quit', 'exit']:
            break
        if type_query == 'random':
            get_random_quote(headers)
        elif type_query == 'keyword':
            str_query = f'https://favqs.com/api/quotes?filter='
            keyword = input('Enter keyword to search quote database for ')
            str_query += keyword
            data, page, last_page = get_json(str_query, headers)
            split_quotes(data, page, collated_data, last_page)
            build_list(collated_data, data, str_query, page, headers)
            if quote_menu(collated_data, keyword, headers):
                break



main()