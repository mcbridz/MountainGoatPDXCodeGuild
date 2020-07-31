#filename lab9-rot13encryption.py
#author Zachary McBride

import personalLibrary

def encrypt(input_string, n):
    #len(encoding_wheel) = 79
    encoding_wheel = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[{]}|;:',<.> "
    output_string = ""
    for char in input_string:
        output_string += encoding_wheel[(encoding_wheel.index(char) + n) % len(encoding_wheel)]
    return output_string


def main():
    
    while True:
        #Welcome and get input for string to be encrypted
        print("Welcome to the ROT(N) encryption program!")
        string_to_be_encrypted = input("Please enter string to be encrypted. ")
        print(f"You have entered: {string_to_be_encrypted}.")
        #get input for degree of encryption (n)
        rotN = personalLibrary.validate_integer(input("Enter rotation factor (counting numbers only: '1' '50' '100'...) "))
        #send string to encryption function
        print(encrypt(string_to_be_encrypted, rotN))
        if input("Would you like to encrypt another string? Press ENTER to continue, type 'quit' to exit program. ") != "":
            break

main()