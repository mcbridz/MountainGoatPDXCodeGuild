#filename: madlib.py
#author: Zachary McBride

welcome = "Welcome to MadLib Valentine Edition!"
instruction = "The Valentine Will Appear As The Roses/Violets Poem"
valStat = "O"
rosStat = "O"
vioStat = "O"
nouStat = "O"
namStat = "O"
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# def three_of(kind):
#     output_list = []
#     for _ in range(3):
#         output_list.append(input(f"Enter a {kind}: "))
#     return output_list
clear()
print(welcome)
print(instruction)
while True:
    valStat = "O"
    rosStat = "O"
    vioStat = "O"
    nouStat = "O"
    namStat = "O"
    for x in range(5):
        inputReq = f'''
        Enter:
        Name of Valentine {valStat}
        Plural Noun (Roses) {rosStat}
        Plural Noun (Violets) {vioStat}
        Plural Noun (Play on words, not 'you') {nouStat}
        Your Name {namStat}
        '''
        selectionsMade = 0
        stats = [valStat, rosStat, vioStat, nouStat, namStat]
        for y in stats:
            if y == "X":
                selectionsMade = selectionsMade + 1

        print(inputReq, flush = True)
        if selectionsMade > 0:
            print("You have made the following choices so far...")
            if selectionsMade == 1:
                print(valentine)
            elif selectionsMade == 2:
                print(valentine)
                print(roses)
            elif selectionsMade == 3:
                print(valentine)
                print(roses)
                print(violets)
            elif selectionsMade == 4:
                print(valentine)
                print(roses)
                print(violets)
                print(gameNoun)
        if x == 0:
            valentine = input("Three names of Valentine names, separated by a comma and space. ")
            valentine = valentine.split(', ')
            valStat = "X"
        elif x == 1:
            roses = input("Three names of a replacement for 'Roses', separated by a comma and space. ")
            roses = roses.split(', ')
            rosStat = "X"
        elif x == 2:
            violets = input("Three names of a replacement for 'Violets', separated by a comma and space. ")
            violets = violets.split(', ')
            vioStat = "X"
        elif x == 3:
            gameNoun = input("Three funny replacements for: 'You love me, and I love...', separated by a comma and space. ")
            gameNoun = gameNoun.split(', ')
            nouStat = "X"
        else:
            signature = input("Your name, for the signature. ")
            namStat = "X"
        clear()
    import random
    while True:
        if input("Would you like to hear a valentine? Enter yes/no.").lower() != "no":
            keep_going = True
            while keep_going == True:
                print(f'''
                Dear {valentine[random.randint(0, 2)]},
                {roses[random.randint(0, 2)]} are red,
                {violets[random.randint(0, 2)]} are blue,
                you love me,
                and I love {gameNoun[random.randint(0, 2)]}!
                From,
                    {signature}
                ''')
                if input("Do you want to hear another valentine from your input? Enter yes/no. ").lower() == "no":
                    keep_going = False
        break
    if input("Flushing cache... would you like to make more valentines? Enter yes/no. ").lower() == "no":
        break
