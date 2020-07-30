#Alternate method of splitting a word into a list of char's
def split(word):
    return [char for char in word]
#Check two words to see if they are anagrams of each other.
def anagramCheck(arg1, arg2):
    word1 = split(arg1).sort()
    word2 = split(arg2).sort()
    if word1 == word2:
        return True
    else:
        return False
from os import system, name
#OS-specific clear-screen <REQUIRES [from os import system, name]>
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
#Validate string as an integer, returns integer
def validate_integer(text):
    while True:
        if text.isdigit():
            return int(text)
        else:
            text = input("Invalid entry, please try again!")
