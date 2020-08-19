#filename lab4-magic8ball.py
#author Zachary McBride

welcome = "Welcome to the Magic 8 Ball! Prepare to be amazed!"

possibilities = {1: "It is certain", 2: "It is decidedly so.", 3: "Without a doubt.", 4: "Yes - definitely}", 5: "You may rely on it.", 6: "As I see it, yes.", 7: "Most Likely", 8: "Outlook good", 9: "Yes.", 10: "Signs point to yes.", 11: "Better not tell you now.", 12: "Don't count on it.", 13: "My reply is no", 14: "My sources say no.", 15: "Outlook not so good.", 16: "Very doubtful."}

def main():
    print(welcome)
    while True:
        question = input("Ask your question... if you dare! ")
        answer = 0
        for i in question:
            answer += ord(i)
        answer = (answer % 16) + 1
        print(possibilities[answer])
        if input("Would you like to play again? Press ENTER to continue, 'quit' to exit. ") != '':
            break

main()
