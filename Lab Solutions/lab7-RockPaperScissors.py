#filename: lab7-RockPaperscissors.py
#author: Zachary McBride

import random

def printRock():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    ''')

def printPaper():
    print('''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

    ''')

def printScissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)    
    ''')

def validate_integer(text):
    while True:
        if text.isdigit():
            return int(text)
        else:
            text = input("Invalid entry, please try again!")

def tie(player, opponent):
    if player == opponent:
        return True
    else:
        return False

def win_paperVS(opponent):
    if opponent == "rock":
        return True
    else:
        return False

def win_scissorsVS(opponent):
    if opponent == "paper":
        return True
    else:
        return False

def win_rockVS(opponent):
    if opponent == "scissors":
        return True
    else:
        return False

def cpu_pick():
    pick = random.randrange(0, 3)
    if pick == 0:
        printRock()
        return "rock"
    elif pick == 1:
        printPaper()
        return "paper"
    else:
        printScissors()
        return "scissors"

def print_score(human_score, cpu_score):
    print(f'''
        {human_score}                          {cpu_score}
    Your Score                 CPU Score
    ''')

def main():
    print("Welcome to ROCK PAPER SCISSORS: Prepare to Die Edition.")
    score1 = 0
    score2 = 0
    while True:
        choice = input("Test your might! Pick rock(0), paper(1), or scissors(2)")
        choice = validate_integer(choice)
        if choice == 0:
            printRock()
            opponent = cpu_pick()
            if tie("rock", opponent):
                print("TIE!")
                print_score(score1, score2)
                continue
            else: 
                if win_rockVS(opponent):
                    score1 += 1
                    print("YOU WIN!!!")
                else:
                    score2 += 1
                    print("YOU LOSE!!!")
        elif choice == 1:
            printPaper()
            opponent = cpu_pick()
            if tie("paper", opponent):
                print("TIE!")
                print_score(score1, score2)
                continue
            else: 
                if win_paperVS(opponent):
                    score1 += 1
                    print("YOU WIN!!!")
                else:
                    score2 += 1
                    print("YOU LOSE!!!")
        else:
            printScissors()
            opponent = cpu_pick()
            if tie("scissors", opponent):
                print("TIE!")
                print_score(score1, score2)
                continue
            else: 
                if win_scissorsVS(opponent):
                    score1 += 1
                    print("YOU WIN!!!")
                else:
                    score2 += 1
                    print("YOU LOSE!!!")
        print_score(score1, score2)
        if (input("Type quit to give up!").lower() == "quit"):
            break

main()
