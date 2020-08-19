#filename: lab12-blackjack_advice.py
#author: Zachary McBride

# Lab 12: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice 
# during a game by asking the player for cards. First, ask the user 
# for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number 
# cards are worth their number, all face cards are worth 10. At this 
# point, assume aces are worth 1. Use the following rules to determine 
# the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

# Version 2 (optional)

# Aces can be worth 11 if they won't put the total point value of 
# both cards over 21. Remember that you can have multiple aces in a 
# hand. Try generating a list of all possible hand values by doubling 
# the number of values in the output whenever you encounter an ace. 
# For one half, add 1, for the other, add 11. This ensures if you have 
# multiple aces that you account for the full range of possible values.

advice = {
    3: "hit",
    4: "hit",
    5: "hit",
    6: "hit",
    7: "hit",
    8: "hit",
    9: "hit",
    10: "hit",
    11: "hit",
    12: "hit",
    13: "hit",
    14: "hit",
    15: "hit",
    16: "hit",
    17: "stay",
    18: "stay",
    19: "stay",
    20: "stay",
    21: "Blackjack!"
}

card_values = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def card_validation(card, card_values):
    """
    Function taking in card<str> and card_values<dict> to validate that the card provided is a possible card, requiring user to input a valid card if not.
    
    Parameters: card<str> card_values<dict>

    output: card<str>
    """
    while card not in card_values:
        card = input("Invalid card selection, please try again. ")
    return card

def get_cards(card_values):
    """
    Function specific to three-card blackjack advice program, using the card_values<dict> to validate user input in-process.

    Parameters: card_values<dict>

    Output: cards<list[3]>
    """
    cards = []
    cards.append(input("What is your first card? "))
    cards[0] = card_validation(cards[0], card_values)
    cards.append(input("What is your second card? "))
    cards[1] = card_validation(cards[1], card_values)
    cards.append(input("What is your third card? "))
    cards[2] = card_validation(cards[2], card_values)
    return cards

def find_total(cards, card_values):
    """
    Function to find possible numerical values from a hand of three cards
    
    Parameters: cards<list-ints>, card_values<dict>
    
    Output: (aces): <int-value>, <int-value> 
    (no aces): <int-value>
    """
    sum = 0
    if 'A' in cards:
        for card in cards:
            sum += card_values.get(card)
        return sum, sum + 10
    else:
        for card in cards:
            sum += card_values.get(card)
        return sum



def blackjack_advice(hand, advice, card_values):
    """
    Function gives advice based on list of cards.
    
    Parameters: hand<list>, advice<dict>, card_values<dict>

    Output: Matched to advice dictionary to determine hit/stay/bust
    """
    
    if 'A' in hand:
        total1, total2 = find_total(hand, card_values)
        if total1 <= 21 and total2 <= 21:
            print(
                f"""
                You have two hands in active play!
                Hand 1 = {total1}, {advice.get(total1, 'Already Busted!')}
                Hand 2 = {total2}, {advice.get(total2, 'Already Busted!')}
                """)
        elif total1 <= 21 or total2 <= 21:
            print(
                f"""
                You have one hand in active play!
                Hand 1 = {total1}, {advice.get(total1, 'Already Busted!')}
                Hand 2 = {total2}, {advice.get(total2, 'Already Busted!')}
                """)
        else:
            print(
                f"""
                You have no hands in active play!
                Hand 1 = {total1}, {advice.get(total1, 'Already Busted!')}
                Hand 2 = {total2}, {advice.get(total2, 'Already Busted!')}
                """)
    else:
        total = find_total(hand, card_values)
        print(f"Your hand is {total}, {advice.get(total, 'Already Busted!')}")

def main(advice, card_values):
    print("Welcome to the Blackjack advice consulting agency! You should not listen to me.")
    while True:
        hand = get_cards(card_values)
        blackjack_advice(hand, advice, card_values)
        if input("Would you like to play again? Press ENTER to continue, <quit> to exit.") != '':
            break
    print("Good-bye!")

main(advice, card_values)