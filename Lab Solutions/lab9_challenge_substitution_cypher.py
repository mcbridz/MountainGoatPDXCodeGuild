#filename: lab9_challenge_substitution_cypher.py
#author: Zachary McBride

import random

#substitution cypher

#cypher generator
def cypher_generator():
    output_dict = {}
    encoding_wheel = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]}|;:'\"\\/,<.>? "
    encoding_list = [char for char in encoding_wheel]
    #print(encoding_list)
    randomizer = random.randint(3, 23)
    multiplier = 0
    while multiplier <= randomizer:
        random.shuffle(encoding_list)
        multiplier += 1
    cypher = ''.join(encoding_list)
    #print(encoding_list)
    for i in range(len(encoding_wheel)):
        #additional_complexity = ""
        # additional_rand_chars = random.randint(0,5)
        # while len(additional_complexity) <= additional_rand_chars:
        #     additional_complexity += encoding_wheel[random.randint(0, (len(encoding_wheel) - 1))]       
        # case = {encoding_wheel[i]: (cypher[i] + additional_complexity)}
        case = {encoding_wheel[i]: (cypher[i])}
        output_dict.update(case)
    # print(output_dict)
    return output_dict


# def decryptor(input):
#     ...
#     #return output   

#encryption function
def encrypt(input, cypher):
    output = ""
    for char in input:
        output += cypher.get(char)
    return output

#main
def main():
    print("Welcome to the randomized substitution cypher.")
    message = input("Please input the string of your choosing for encryption.")
    cypher = cypher_generator()
    print(encrypt(message, cypher))

main()    
