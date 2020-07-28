#filename: lab5-random_emoticon_generator.py
#author: Zachary McBride

eyes = ['ಠ', '•', '◕', '°', '☉', '◉']
noses = ['੪', 'д', 'ᔕ', 'ヘ', ' ͜ ', 'ᓀ']
left_head = ['|', '{', '(', ';', '༼', ':']
right_head = ['|', '}', ')', ';', '༽', ':']

import random

def generate_face():
    head_alignment = random.randrange(0, len(left_head))
    eye_alignment = random.randrange(0, len(eyes))
    return left_head[head_alignment] + " " + eyes[eye_alignment] + " " + random.choice(noses) + " " + eyes[eye_alignment] + " " + right_head[head_alignment]

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