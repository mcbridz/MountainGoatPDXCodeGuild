# Problem 5
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).


# this_is_snake_case (python)
# thisIsCamelCase (java, javascript, c#)
# ThisIsPascalCase (python classes)
# this-is-kebab-case (css)


#text.replace(char.ascii)
#string.ascii_punctuation()

import string


def snake_case(text):
    output_string = ''
    for char in text:
        if char not in string.punctuation:
            output_string += char
    output_string = output_string.lower()
    output_string = output_string.replace(' ', '_')
    #text = text.replace(string.punctuation, '')
    return output_string
#print(snake_case('@Hello % World!@#$!')) # hello_world
#print(string.punctuation)


# Problem 6

# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).




def camel_case(text):
    output_string = ''
    text = text.lower() 
    #remove punctuation
    for char in text:
        if char == ' ' or char not in string.punctuation:
            output_string+= char
    output_string_the_second = ''
    list_output = output_string.split(' ')
    for i in range(len(list_output)):
        list_output[i] = list_output[i].capitalize()    
    list_output[0] = list_output[0].lower()
    output_string_the_second = ''.join(list_output)
    #
    # for i in range(len(output_string) - 1): #last letter?
    #     if output_string[i] == ' ':
    #         output_string_the_second += output_string[i+1].upper()
    #         i += 1
    #     else:
    #         output_string_the_second += output_string[i]
    return output_string_the_second   
print(camel_case('Hello World!')) # helloWorld
print(camel_case('This is another example.')) # thisIsAnotherExample



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

