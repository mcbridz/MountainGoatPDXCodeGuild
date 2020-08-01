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


#Truncates <n> float to <decimals> decimals place.
#Use negative numbers to truncate left of decimal
#truncate(n<float>, decimals<int>=0:default)
def truncate(n, decimales=0):
    multiplier = 10 ** decimales
    return int(n * multiplier) / multiplier
#input = 1000000

#Work Function
#Takes string input, converts to list, inserts commas, then returns as list
#make_pretty_helper(<string>) = list[<num_chars>]
def make_pretty_helper(input):
    output = input
    if len(output) < 4:
        return output
    output = [char for char in output]
    decrementer = len(output) - 3
    while decrementer >= 0:             #01234567
        output.insert(decrementer, ',') #1000000                          
        decrementer -= 3                #1000,000

    #print(output)

    return output

#quiet return
#make_pretty(<int input>):str output
def make_pretty(input):
    check_num = int(input)
    if type(check_num) == int:
        return make_pretty_helper(input)
    else:
        return "NaN"

