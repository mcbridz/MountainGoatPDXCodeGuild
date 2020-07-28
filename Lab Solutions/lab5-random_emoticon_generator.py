#filename: lab5-random_emoticon_generator.py
#author: Zachary McBride

eyes = ['ಠ', '•', '◕', '°', '☉', '◉']
noses = ['੪', 'д', 'ᔕ', 'ヘ', ' ͜ ', 'ᓀ']
left_head = ['|', '{', '(', ';', '༼', ':']
right_head = ['|', '}', ')', ';', '༽', ':']

import random

def generate_face():
    return random.choice(left_head) + random.choice(eyes) + random.choice(noses) + random.choice(eyes) + random.choice(right_head)

def main():
    num = int(input(("Please enter the number of faces to be generated.")))
    while num > 0:
        print(generate_face())
        num -= 1
    print("...and remember, Pikachu is watching!")
    print('''
█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█ 
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀
    ''')
main()