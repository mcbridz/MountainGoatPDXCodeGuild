import string
def get_text(file_name):
    '''
        This function will read file_name
        and return its contents as a string.
    '''
    with open(file_name, "r") as file:
        text = file.read().lower()
    return text

def most_frequent(word_dict):
    '''
        This function takes in a dictionary and sorts the words
        by their value, then returns a dictionary with the ten most
        frequently occuring words
    '''
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    
    top_ten = []
    
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        top_ten.append(words[i])

    top_ten = dict(top_ten) # convert list of tuples into a dictionary

    return top_ten

def main():
    # Your code goes here
    alice = get_text("countwords.txt")
    alice.replace("\n", " ")
    alice = alice.translate(str.maketrans('','',string.punctuation))
    alice = alice.split()
    freq = dict()
    for x in alice:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    print(most_frequent(freq))


main()