#filename lab8-guess-a-number.py
#author Zachary McBride

import personalLibrary
import random
from os import system, name



instructions = '''
Welcome to GUESS A NUMBER!
The game where you attempt to fathom the infinite genius
and unpredictability of a computerized random guess of a
single number between 1 and 10 (indicated on the below 
number line).
As you guess numbers, the "guess line" of all zeroes will
populate with ones to help you keep track of your 
guesses.

Begin!
'''

# def reset(list_of_guesses, guesses):
#     for i in list_of_guesses:
#         i = 0
#     guesses = 0

def print_guesses_and_lines(list_of_guesses, number_line, guesses):
    print(list_of_guesses)
    print(number_line)
    #print(solution_line)
    print(f"Guesses: {guesses}")

def mark_guess(human_guess, guesses, list_of_guesses):
    list_of_guesses[human_guess - 1] = 1
    guesses += 1
    return guesses

def make_target(solution_line):
    solution_line[random.randint(1, 10) - 1] = 1
    print("The computer has selected a number that you cannot even fathom!")

def final_check(list_of_guesses, solution_line):
    i = 0
    while i < 10:
        if list_of_guesses[i] == solution_line[i]:
            return False
        i += 1
    return True

def fetch_target(solution_line):
    return solution_line.index(1)

def are_you_closer(arg1, arg2, solution_line):
    target = fetch_target(solution_line) + 1
    if (abs(arg1 - target) < abs(arg2 - target)):
        print("Getting warmer!")
    else:
        print("Getting colder!")
    if abs(arg1 - target) < 2:
        print("You're red hot!")
    elif abs(arg1 - target) > 5:
        print("You're ice cold!") 

def declare_winner(solution_line):
    print(f"Congratulations! You guessed the correct number!\nThe computer chose {str(fetch_target(solution_line) + 1)}")


import time
# time.sleep(2)

def main():
    while True:
        list_of_guesses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        number_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        solution_line = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        guesses = 0
        trailing_guess = ''
        print(instructions)
        make_target(solution_line)
        while True:
            # print_guesses_and_lines(list_of_guesses, number_line, guesses)
            guess = 0
            while not 1 <= guess <= 10 :
                guess = personalLibrary.validate_integer(input("Guess a number between 1 and 10!"))
            guesses = mark_guess(guess, guesses, list_of_guesses)
            print_guesses_and_lines(list_of_guesses, number_line, guesses)
            if final_check(list_of_guesses, solution_line):
                # personalLibrary.clear()
                #print(trailing_guess)
                if trailing_guess != '':
                    are_you_closer(guess, trailing_guess, solution_line)
                    trailing_guess = guess
                else:
                    trailing_guess = guess
                if final_check(list_of_guesses, solution_line):
                    pass
                else:
                    break
            else:
                break
 #           time.sleep(4)
        declare_winner(solution_line)
        if input("Type 'quit' to quit, ENTER to play again.") == "quit":
            break
        #reset(list_of_guesses, guesses)
        personalLibrary.clear()
        
            
        

main()