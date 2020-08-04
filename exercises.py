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
    outcome = None
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

def remove_empty(mylist):
    while True:
        try:
            mylist.remove('')
        except:
            return mylist

print(remove_empty(['a','b','','c','','d']))

