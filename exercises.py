# Problem 5
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).


# this_is_snake_case (python)
# thisIsCamelCase (java, javascript, c#)
# ThisIsPascalCase (python classes)
# this-is-kebab-case (css)


#text.replace(char.ascii)
#string.ascii_punctuation()

# import string


# def snake_case(text):
#     output_string = ''
#     for char in text:
#         if char not in string.punctuation:
#             output_string += char
#     output_string = output_string.lower()
#     output_string = output_string.replace(' ', '_')
#     #text = text.replace(string.punctuation, '')
#     return output_string
# #print(snake_case('@Hello % World!@#$!')) # hello_world
# #print(string.punctuation)


# # Problem 6

# # Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).




# def camel_case(text):
#     output_string = ''
#     text = text.lower() 
#     #remove punctuation
#     for char in text:
#         if char == ' ' or char not in string.punctuation:
#             output_string+= char
#     output_string_the_second = ''
#     list_output = output_string.split(' ')
#     for i in range(len(list_output)):
#         list_output[i] = list_output[i].capitalize()    
#     list_output[0] = list_output[0].lower()
#     output_string_the_second = ''.join(list_output)
#     #
#     # for i in range(len(output_string) - 1): #last letter?
#     #     if output_string[i] == ' ':
#     #         output_string_the_second += output_string[i+1].upper()
#     #         i += 1
#     #     else:
#     #         output_string_the_second += output_string[i]
#     return output_string_the_second   
# print(camel_case('Hello World!')) # helloWorld
# print(camel_case('This is another example.')) # thisIsAnotherExample



# mylist = ['apples', 'bananas', 'pears']
# mylist[0] = 'cherries'
# for i in range(len(mylist)):
#     mylist[i] = mylist[i].capitalize()
#     #mylist[i] = mylist[i] + '!'
# print(mylist)


# x = mylist[0]
# x = 'hello!'
# print(mylist[0])

# for element in mylist:
#     element = 'hello!'
# print(mylist)

# tester_string = "I love pizza!"
# list_strings = tester_string.split(" ")
# print(list_strings)
# joined_strings = ''.join(list_strings)
# print(joined_strings)

#"abcdefg"

#       01234
# text = 'hello'
# for char in text:
#     print(char)
# for i in range(len(text)):
#     print(i, text[i])
# 0123
#'hihi'
# def count_hi(text):
#     count = 0
#     for i in range(len(text)-1):
#         # print(len(text), i, i+1)
#         # text[i+1]
#         if text[i] == 'h' and text[i+1] == 'i':
#             count += 1
#     return count
















#random_list(n) generates and returns a list of length n, with 
#random values between 0 and 100
import random
import time
# seed = time.time()
# print('the seed is', seed)
# random.seed(seed)
def random_list(n): #5! = 5*4*3*2*1
    output = []
    while len(output) < n:
        output.append(random.randint(0, 100))
    return output




#shuffle(nums) randomly re-arranges a list
#       1 iterate through the indices of the list
#       2 for each index, generate a random index
#       3 swap the elements at the two indices
def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums) - 1)
        # print(i, j)
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp


#is_sorted(nums) checks if a list is sorted
#Iterate through the indices of the list
#if the element at the current index is greater than the 
#element at the next index, the list isn't sorted, and you can return False
#if you get through the entire list and each element is 
#less than or equal to the next element, the list is sorted, and you can return True
#0123456789
def is_sorted(nums):
    outcome = None
    for i in range(len(nums) - 1):     #(0, 1) versus (0, 1, 2)
        if nums[i] > nums[i+1]:        #
            return False
        else:
            outcome = True
    return outcome

#bogosort(nums) continues to generate random arrangements 
#until the list is sorted
def bogosort(nums):
    # if is_sorted(nums):
    # shuffle(nums)
    # if is_sorted(nums):
    #     return
    # shuffle(nums)
    # if is_sort(nums):
    #     return
    # shuffle(nums)
    #outcome = None
    start_time = time.time()
    tries = 0
    # while outcome != True:
    #     shuffle(nums)
    #     outcome = is_sorted(nums)
    #     tries += 1
    # print(tries)

    while not is_sorted(nums):
        shuffle(nums)
        tries += 1
    
    end_time = time.time()
    print('that took', (end_time - start_time)/tries, 'seconds')
    return tries
    


    

# print(bogosort([8, 5, 2, 7, 9, 1]))
# nums = random_list(9)
# bogosort(nums)
# print(nums)

# nums.sort()
# print(nums)
# shuffle(nums)
# nums.sort()
# print(nums)

# print(is_sorted([1,2,3]))
# print(is_sorted([2,1,3]))
# print(is_sorted([1,3,2]))

# tries_per_list_length = 50
# for list_length in range(2, 9):
#     total = 0
#     for i in range(tries_per_list_length):
#         nums = random_list(list_length)
#         total += bogosort(nums)
#     total /= tries_per_list_length
#     print('list length',list_length,total)


# import time
# print(time.time())

# def remove_empty(mylist):
#     while True:
#         try:
#             mylist.remove('')
#         except:
#             return mylist

# print(remove_empty(['a','b','','c','','d']))

# car = {

# }

# x = car.items()

# print(x)


# Problem 3: Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. 
# racecar. Another way to think of it is as a word that's equal to 
# its own reverse. Write a function check_palindrome(word) which 
# takes a string, and returns True if the string's a palindrome, 
# or False if it's not.

def check_palindrome(word):
    word_list = list(word)
    reversed_word_list = list(reversed(word))

    #comparison method
    # print(reversed_word_list)
    # if word_list == reversed_word_list:
    #     return True
    # return False

    #iterable method
    # for i in range(len(word_list)):
    #     if word_list[i] != reversed_word_list[i]:
    #         return False
    # return True


    #single iterable with n-length method
    # for f in range(len(word)//2):
    #     b = len(word) - f - 1
    #     if word[f] != word[b]:
    #         return False
    # return True

    return word == ''.join(reversed(word))

    

# print(check_palindrome('racecar')) # True
# print(check_palindrome('palindrome')) # False



# iterables
# can be used with a for loop
# can be converted to a list
# string, list, tuple, dictionary, range, reverseiterator that reverse returns, dict_keys, dict_values, dict_items

# print(list('hello'))
# print(list(range(10)))
# for element in [{'a': 1}, {'b': 2}]:
#     print(element)

# for char in string
# for element in list
# for element in tuple
# for key in dictionary

# prices = {'apples': 1.0, 'bananas': 0.5, 'cherries': 2.0}
# print(list(prices.values()))
# for value in prices.values():
#     print(value)

# result = str(list(range(10)))
# print(result)

# Problem 4: Anagram
# Two words are anagrams of eachother if the letters of one can 
# be rearranged to fit the other. e.g. anagram and nag a ram. 
# Write another function check_anagram(word1, word2) that takes 
# two strings as parameters and returns True if they're anagrams 
# of eachother, False if they're not. The procedure for comparing 
# the two strings is as follow:

# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
def check_anagram(word1, word2):
    word1_sorted = [char.lower() for char in word1 if char != ' ']
    word2_sorted = [char.lower() for char in word2 if char != ' ']
    word1_sorted.sort()
    word2_sorted.sort()
    # print(word1_sorted)
    # print(word2_sorted)
    return word1_sorted == word2_sorted

# print(check_anagram('anagram', 'nag a ram')) # True
# print(check_anagram('sheep', 'goat')) # False

# Hello, my name isn't Zach!
# ["hello": "\,"", " my name isn": "\'"", "t Zach": !]


# Problem 5: Scramble Letters
# Write a function scramble_letters to scramble the internals 
# letters of words, but keep first and last letter the same.
import string
def scramble_letters(text):
    words = text.split()
    list_scrambled = []
    for word in words:
        if len(word) < 4:
            list_scrambled.append(word)
            continue
        word_scrambled = ""
        word_scrambled += word[0]
        temp_list = list(word)
        temp_list = temp_list[1:len(word) - 1]
        # print(temp_list)
        random.shuffle(temp_list)
        word_scrambled += ''.join(temp_list)
        word_scrambled += word[len(word)-1]
        list_scrambled.append(word_scrambled)
    return ' '.join(list_scrambled)

            

        
print(scramble_letters('hello world this is easier')) # hlelo wlrod tihs is esiaer




# Problem 6
# Write a function cart_total to calculate the total of a shopping cart.

def cart_total(prices, cart):
    total = 0
    for item in cart:
        total += prices[item['item']] * item['quantity']
    return total
prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
cart = [{'item': 'apples', 'quantity': 3}, {'item': 'kiwis', 'quantity': 4}]
# print(cart_total(prices, cart)) # 11.0