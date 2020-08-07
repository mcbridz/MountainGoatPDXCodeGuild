#filename: lab14-number_to_phrase.py
#author: Zachary McBride

# Lab 14: Number to Phrase

# Convert a given number into its English representation. For example: 67 becomes 
# 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10

# Hint 2: use the digit as an index for a list of strings or the key in a dictionary.
# Version 2

# Handle numbers from 100-999.

# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.

ones_not_teens = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

tweens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens_not_tweens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

distal_digits = {
    3: "hundred",
    4: "thousand",
    5: "thousand",
    6: "thousand",
    7: "million",
    8: "million",
    9: "million",
    10: "trillion"
}

def number_of_digits(input_num):
    """
    Function where input_num is converted to a string, then returns the length of that string.

    Parameters: input_num<int>

    Output: digits_of_input_num<int>
    """
    len(str(input_num))

def hundreds_translate(input_num):
    """
    Function where input_num, where input_num is between 1 and 100, returning translated string.

    Parameters: input_num<int>

    Outpu: return_string<str>
    """
    list_num = list(str(input_num))
    int_num = input_num
    # first_significant_digit = 0
    if int_num < 10:
        return ones_not_teens[int_num]
    elif int_num < 20:
        return tweens[int_num]
    elif int_num < 100:
        return_string = ""
        return_string += tens_not_tweens[int(list_num[len(list_num) - 2])]
        if int_num % 10 != 0:
            return_string += f"-{ones_not_teens[int_num % 10]}"
        return return_string
    else:
        return_string = ""
        return_string += ones_not_teens[int(list_num[0])]
        return_string += " hundred"
        if list_num[1] == '0' and list_num[2] == '0':
            return return_string
        if list_num[1] == '0':
            return_string += " and "
            return_string += ones_not_teens[int(list_num[2])] 
            return return_string           
        elif list_num[1] == '1':
            return_string += f" {tweens[10 + int(list_num[2])]}"
            return return_string
        else:
            return_string += f" {tens_not_tweens[int(list_num[1])]}-{ones_not_teens[int(list_num[1])]}"
            return return_string
        return return_string
        

def break_and_translate(input_num):
    """
    Function where input_num is made into a list, padded with front-zeroes until filling the current 'hundred' or three digit block is filled, then translates each block of three until complete.

    Parameters: input_num<int>

    Output: return_string<str>
    """
    int_num = input_num
    list_num = list(str(input_num))
    num_digits = len(list_num)
    while len(list_num)%3 != 0:
        list_num.insert(0, '0')
    return_string = ""
    i = len(list_num)
    while i > 0:           
        # broken_off_hundreds = list_num[i-3:i]  #list slicing non-inclusive on upper-bound
        # broken_off_hundreds = ''.join(broken_off_hundreds)
        # broken_off_hundreds = int(broken_off_hundreds)
        broken_off_hundreds = int(''.join(list_num[i-3:i]))      #012345678
        return_string += hundreds_translate(broken_off_hundreds) #001234567
        i -= 3


    return return_string


print(hundreds_translate(5))
print(hundreds_translate(13))
print(hundreds_translate(59))
print(break_and_translate(5))
print(break_and_translate(13))
print(break_and_translate(59))
print(hundreds_translate(530))
print(hundreds_translate(700))
print(hundreds_translate(701))
print(hundreds_translate(855))