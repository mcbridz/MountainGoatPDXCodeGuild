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
    1: "",
    2: " thousand",
    3: " million",
    4: " billion",
    5: " trillion",
    6: " quadrillion"
}

def number_of_digits(input_num):
    """
    Function where input_num is converted to a string, then returns the length of that string.

    Parameters: input_num<int>

    Output: digits_of_input_num<int>
    """
    len(str(input_num))

def hundreds_translate(input_num, triplets):
    """
    Function where input_num, where input_num is between 1 and 100, returning translated string.

    Parameters: input_num<int>

    Output: return_string<str>
    """
    if input_num == 0:
        return ""
    list_num = list(str(input_num))
    int_num = input_num
    return_string = ""
    if int_num < 10:
        if triplets <= 1:
            return_string += " and "
        return_string += ones_not_teens[int_num]
        if triplets > 1:
            return_string += f"{distal_digits[triplets]} "
        return return_string
    elif int_num < 20:
        return_string += tweens[int_num]
        return_string += f"{distal_digits[triplets]} "
        return return_string
    elif int_num < 100:
        return_string += tens_not_tweens[int(list_num[0])]
        if list_num[1] != 0:
            return_string += '-'
            return_string += ones_not_teens[int(list_num[1])]
        return_string += f"{distal_digits[triplets]} "
        return return_string
    else:
        return_string += ones_not_teens[int(list_num[0])]
        return_string += " hundred"
        if list_num[1] == '0' and list_num[2] == '0':
            return_string += distal_digits[triplets]
            return return_string
        if list_num[1] == '0':
            return_string += " and "
            return_string += ones_not_teens[int(list_num[2])] 
            return_string += f"{distal_digits[triplets]} "
            return return_string           
        elif list_num[1] == '1':
            return_string += f" {tweens[10 + int(list_num[2])]}"
            return_string += f"{distal_digits[triplets]} "
            return return_string
        else:
            return_string += f" {tens_not_tweens[int(list_num[1])]}-{ones_not_teens[int(list_num[2])]}"
            return_string += f"{distal_digits[triplets]} "
            return return_string
        return return_string
        

def break_and_translate(input_num):
    """
    Function where input_num is made into a list, padded with front-zeroes until filling the current 'hundred' or three digit block is filled, then translates each block of three until complete.

    Parameters: input_num<int>

    Output: return_string<str>
    """
    if input_num == 0:
        return ""
    int_num = input_num
    list_num = list(str(input_num))
    while len(list_num)%3 != 0:
        list_num.insert(0, '0')
    return_string = ""
    i = 0
    triplets = len(list_num) // 3
    while i < len(list_num) - 1:
        broken_off_hundreds = int(''.join(list_num[i:i+3]))      #012345678
        return_string += hundreds_translate(broken_off_hundreds, triplets) #001234567
        triplets -= 1
        i += 3


    return return_string


# print(hundreds_translate(5, 1))
# print(hundreds_translate(13, 1))
# print(hundreds_translate(59, 1))
# print(break_and_translate(5))
# print(break_and_translate(13))
# print(break_and_translate(59))
# print(hundreds_translate(530, 1))
# print(hundreds_translate(700, 1))
# print(hundreds_translate(701, 1))
# print(hundreds_translate(855, 1))
# print(break_and_translate(100))
# print(break_and_translate(1000))
# print(break_and_translate(1210))
# print(break_and_translate(50243))
# print(break_and_translate(123456789)) #123,456,789
# print(break_and_translate(100000000))
# print(break_and_translate(100000001))

# print("Welcome to the number translator!")
# while True:
#     input_num = input("Enter a number between one(1) and nine hundred and ninety-nine trillion(999,999,999,999,999) ")
#     input_num = int(input_num)
#     translated_num = break_and_translate(input_num)
#     print(f"You entered {input_num}. That is translated to: \n\t {translated_num}")
#     if input("Press ENTER to continue, or type anything to quit. ") != "":
#         break

for i in range(int(10e7) + 2, int(10e8), 137):
    print(break_and_translate(i))