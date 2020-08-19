#filename: lab6-passwordGenerator.py
#author: Zachary McBride

#chr(n) = int-> ASCII

import random

def generateUpper():
    return chr(random.randrange(65, 91))

def generateLower():
    return chr(random.randrange(97, 123))

def generateSpChr():
    return chr(random.randrange(33, 48))

def generateNum():
    return random.randrange(0,10)

def split(word):
    return [char for char in word]


def main():    
    while True:
        length = 0
        upper = 0
        lower = 0
        nums = 0
        specs = 0
        def status():
            print(f'''
            length : {length}
            uppers : {upper}
            lowers : {lower}
            nums   : {nums}
            specs  : {specs}
            ''')
        status()
        length = int(input("How long of a password would you like?" ))
        status()
        upper = int(input("How many upper-case?" ))
        status()
        lower = int(input("How many lower-case?" ))
        status()
        nums = int(input("How many numbers?" ))
        status()
        specs = int(input("How many special chars?" ))
        status()
        if (upper + lower + nums + specs) != length:
            print("Your numbers do not add up, please try again.")
            r = input("Press ENTER to restart or type exit to end program ")
            if r != '':
                break
            continue
        password = ''
        for i in range(upper):
            password += generateUpper()
        for i in range(lower):
            password += generateLower()
        for i in range(nums):
            password += str(generateNum())
        for i in range(specs):
            password += generateSpChr()
        password = split(password)
        shufflingTime = random.randrange(0, 9)
        shufflingTime *= 17
        for i in range(shufflingTime):
            random.shuffle(password)
        final_password = ''.join(password)
        print(final_password)
        if input("Would you like another password? (y/n)") != 'y':
            break

            
            

main()       
            

                