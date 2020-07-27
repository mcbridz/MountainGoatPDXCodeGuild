#filename: madlib.py
#author: Zachary McBride

welcome = "Welcome to MadLib Valentine Edition!"
instruction = "The Valentine Will Appear As The Roses/Violets Poem"
valStat = "O"
rosStat = "O"
vioStat = "O"
nouStat = "O"
namStat = "0"
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
print(welcome)
print(instruction)
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
        valentine = input("Name of Valentine ")
        valStat = "X"
    elif x == 1:
        roses = input("Name of a replacement for 'Roses' ")
        rosStat = "X"
    elif x == 2:
        violets = input("Name of a replacement for 'Violets' ")
        vioStat = "X"
    elif x == 3:
        gameNoun = input("Funny replacement for: 'You love me, and I love...' ")
        nouStat = "X"
    else:
        signature = input("Your name, for the signature. ")
        namStat = "X"
    clear()
print(f'''
Dear {valentine},
{roses} are red,
{violets} are blue,
you love me,
and I love {gameNoun}!
From,
     {signature}
''')