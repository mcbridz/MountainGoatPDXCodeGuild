# Problem 1

# Get a string from the user, print out another string, doubling every letter.

# split
# fruits = 'apples, bananas, pears'
# fruits = fruits.split(', ')
# print(fruits)

# fruits = '_'.join(fruits)
# print(fruits)


# text = 'hello'
# output = []
# for char in text:
#     output.append(char)
# print(output)

# output = ''
# for i in range(10):
#     output += str(i)
# print(output)


def double_letters(word):
    #word_output = ''
    word_output = []
    for letter in word:
        word_output.append(letter + letter)
    word_output = ''.join(word_output)
    return word_output




print(double_letters('hello')) # hheelllloo
