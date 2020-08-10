#filename: lab15-count_words.py
#author: Zachary McBride

# Lab 15: Count Words
# Let's write a python module to analyze a given text file containing a book for
# its vocabulary frequency and display the most frequent words to the user in the 
# terminal. Remember there isn't any "perfect" way to identify a word in english 
# (acronymns, mr/ms, contractions, etc), try to find rules that work best.

# Find a book on Project Gutenberg and navigate to the plain-text version. You 
# can then send a request to that url using the requests library to get the text 
# into Python. You can also save the file into the same folder as the .py file 
# and open it using with.

# import requests
# response = requests.get('http://www.gutenberg.org/cache/epub/17192/pg17192.txt')
# print(response.text)
# We can also download a file of english words and place it next our .py file and 
# load it like so:

# with open('the_raven.txt', 'r') as file:
#     text = file.read()
# print(text)
# Take the following steps to build up our dictionary. The result should look 
# something like {'a': 3, 'the': 4}

# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn't 
# in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the 
# code below.

# # word_dict is a dictionary where the key is the word and the value is the count

# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, 
# based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them,
# whichever is smaller

#     print(words[i])

# Version 2 (optional)
# Count how often each unique pair of words is used, then print the top 10 most 
# common pairs with their counts.

# Version 3 (optional)
# Let the user enter a word, then show the words which most frequently follow it.

#################################Begin my lab####################################

#setup
import requests
import string

def get_rid_of_commas_and_periods(word):
    # Function to take in a string, and return a string with all commas and periods removed
    list_word = [char for char in word]
    for char in list_word:
        if char == '.' or char == ',':
            list_word.remove(char)
    return ''.join(list_word)
# print(get_rid_of_commas_and_periods("fine."))
# print(get_rid_of_commas_and_periods("hello,"))

def is_there_no_punctuation(word):
    # Function to take in a word, cycle through a list of its char's and if punctuation found return False
    list_word = [char for char in word]
    for char in list_word:
        if char not in string.ascii_letters:
            return False
    return True
# print(is_there_no_punctuation("ad@v"))
# print(is_there_no_punctuation("dfes"))
# print(is_there_no_punctuation("a"))



#################version 1 dict build code###################################
def build_dict_of_word_frequency(response_text, ignored_words):
    # Function takes in full text of request, split it into a list of words, then cycle through each word and determine if the word is valid before checking/adding/updating the output dictionary.
    list_words = response_text.split()
    dict_words = {}
    for word in list_words:
        # First remove all instances of sentance structure
        temp_word = get_rid_of_commas_and_periods(word)
        # Then check to see if punctuation remains
        if is_there_no_punctuation(temp_word):
            # Then check the word for whether it is already in the dict, or in the ignored words
            if temp_word not in dict_words and temp_word not in ignored_words:
                case = {temp_word: 1}
                dict_words.update(case)
            # Otherwise, if the word has no punctuation, and is in the dict, then add an instance
            elif word in dict_words:
                dict_words[word] += 1
    return dict_words


#################version 1 print code#########################################
def word_instances_printer(response_text, ignored_words):
    dict_words = build_dict_of_word_frequency(response_text, ignored_words)
    words = list(dict_words.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, 
    # based on count
    print("The top ten words used in the text are: ")
    for i in range(min(10, len(words))):
        print(words[i])  # print the top 10 words, or all of them,
    # whichever is smaller
    print("\n")
    
# print(dict_words)
##############################################################################

# version2

# test code for verifying tuple comparisons
# check1 = tuple(("are", "you"))
# check2 = tuple(("are", "you"))
# if check1 == check2:
#     print("Same")
# else:
#     print("Different")

def build_dict_of_word_pairs(response_text):
    list_words = response_text.split()
    paired_words = {}
    i = 0
    while i < len(list_words) - 1:
        if is_there_no_punctuation(get_rid_of_commas_and_periods(list_words[i])):
            if is_there_no_punctuation(get_rid_of_commas_and_periods(list_words[i+1])):
                temp_tuple = tuple(
                        (
                        get_rid_of_commas_and_periods(list_words[i]), 
                        get_rid_of_commas_and_periods(list_words[i+1])
                        )
                    )
                if temp_tuple not in paired_words:
                    case = {temp_tuple: 1}
                    paired_words.update(case)
                else:
                    paired_words[temp_tuple] += 1
        i += 1
    return paired_words

# test code
# print(paired_words)


#######################Version 2 sort-and-display algorithm#####################
def word_pairs_printer(reponse_text):
    paired_words = build_dict_of_word_pairs(reponse_text)
    word_pairs = list(paired_words.items()) # .items() returns a list of tuples
    word_pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, 
    # based on count
    print("The top ten word pairs in the text are: ")
    for i in range(min(10, len(word_pairs))):
        print(word_pairs[i])  # print the top 10 words, or all of them,
    print("\n")

response = requests.get('http://www.gutenberg.org/cache/epub/17192/pg17192.txt')
response_text = response.text.lower()

# To get more significant words from the list, this list of words will be ignored for single
# word dictionaries, but not the paired words dictionary
ignored_words = ["a", "the", "he", "she", "but", "to", "in", "of", "and", "or", "i", 
    "is", "his", "hers", "for", "as", "it", "by", "was", "at", "my", "be", "are", "from",
    "you", "on", "this", "with", "no", "its", "any", "not", "that", "an", "if"]
list_words = response_text.split()
# print(list_words)

############################Demo Code For Both Strategies################################
word_instances_printer(response_text, ignored_words)
word_pairs_printer(response_text)

####################REPL##################
while True:
    preceding_word = input("Please type the word you would like to check for following words: ").lower()
    #reuse existing code
    paired_words = build_dict_of_word_pairs(response_text)
    print(f"The following words follow your chosen word of {preceding_word}: ")
    temp_paired_words = paired_words
    #pull off all keys into a list of strings
    temp_tuples = [pairs for key in temp_paired_words for pairs in key]
    # print(temp_tuples)
    i = 0
    found_any = False
    # accounting for forward checking past range
    while i < len(temp_tuples) - 2:
        # indicates that the word being checked is in the correct position
        if i % 2 == 0 and temp_tuples[i] == preceding_word:
            #print following word from preceding word
            print(temp_tuples[i+1] + ',')
            found_any = True
        if found_any == False:
            print("No matching words were found.")
        i += 1
    print()
    if input("Press ENTER to continue, type quit to exit program. ") != "":
        break