#filename lab11-make_change.py
#author Zachary McBride

#Lab 11: Make Change

#Let's convert a dollar amount into a number of coins. The input will be the total 
# amount, the output will be the number of quarters, dimes, nickles, and pennies. 
# Always break the total into the highest coin value first, resulting in the fewest 
# amount of coins. For this, you'll have to use floor division //, which throws away 
# the remainder. 10/3 is 3.333333, 10//3 is 3.

#Version 2 
# Instead of hard-coding the coins, store them in a list of tuples. This way you can make 
# custom coins.

#example output:
#Welcome to the Change Maker 5000 (tm)
# Enter a dollar amount: 1.36
# 5 quarters, 1 dime, and 1 penny
# Would you like make more change? yes
# Enter a dollar amount: 0.67
# 2 quarters, 1 dime, 1 nickel, 2 pennies
# Would you like make more change? no
# Have a good day!

coins = [
    ('half-dollars', 50),
    ('quarters', 25),
    ('dimes', 10),
    ('nickels', 5),
    ('pennies', 1)
]

import string
def pad_money_with_zeroes(num_input):
    output = str(num_input)
    index_of_decimal = num_input.find('.')
    delta_strings = 2 - len(num_input) + 1 + index_of_decimal
    if delta_strings > 0: #2 - ((1. -> 2) - 1 - (1. -> 1)) 
        pad_zeroes = '0'*delta_strings
        output += pad_zeroes
    return output

#function to find number of 'X' coins in 'total'
def number_of_coinX_in(total, coin):
    output = total // coin    
    return output

#function takes in user-defined 'total' and global list of tuples 'coins', no return value
#print is built into this function
def make_change(total, coins):
    if total.find('.') == -1:
        total += '.00'
    #take total, convert from string to float, multiply by 100 to have values on the 
    #same order as the tuple values, then round, because computers to weird things with
    #floats meant to approximate whole numbers
    running_total = round(float(total) * 100)

    #index runner for 'coins' list of tuples
    i = 0

    #start building output string, to match output example with exercise
    output_string = "There are: "

    #main loop, will continue to run until all divisions occur
    while running_total > 0:

        # debug code prior to implementing single-string method
        # print(f"There are {round(number_of_coinX_in(running_total, coins[i][1]))} {coins[i][0]} in ${total}")

        # if there are >0 of a certain coin in the fed running_total
        if round(number_of_coinX_in(running_total, coins[i][1])) > 0:

            #add "<int> <coins>"
            output_string += f"{round(number_of_coinX_in(running_total, coins[i][1]))} {coins[i][0]}"
            
            #remove that number of coins from the running_total
            running_total -= number_of_coinX_in(running_total, coins[i][1])*coins[i][1]

            #grammatical additions to string output
            if running_total > 0:
                output_string += ", "
            else:
                output_string += " "
        i += 1
    
    #completing single-string method with grammatically correct ending.
    output_string += f"in ${pad_money_with_zeroes(total)}."
    print(output_string)
    return

def main(coins):
    print("Welcome to your neighborhood change-maker! Useful mostly to arcades.")
    while True:
        total = input("How much money would you like to change from useful paper to useless metal? ")
        make_change(total, coins)
        # make_change(1.01, coins)
        if input("Press ENTER to continue, type <quit> to quit.") != "":
            return

main(coins)