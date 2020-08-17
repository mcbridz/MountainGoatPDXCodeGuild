#filename: lab18-atm.py
#author: Zachary McBride

# Lab 18: ATM
# Let's represent an ATM with a class containing two attributes: 
# a balance and an interest rate. A newly created account will 
# default to a balance of 0 and an interest rate of 0.1%. Implement 
# the initializer, as well as the following functions:

# balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't 
#   put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

# Version 2
# Have the ATM maintain a list of transactions. Every time the user makes
#  a deposit or withdrawal, add a string to a list saying 
# 'user deposited $15' or 'user withdrew $15'. Add a new method 
# print_transactions() to your class for printing out the list of transactions.

class ATM:
    def __init__(self):
        self.transaction_history = []
        self.current_balance = float(0)
        self.interest_rate = 0.1
        self.num_transactions = 0
        self.note_translation = {'withdraw': 'withdrew', 'deposit': 'deposited', 'interest': 'received interest of '}
    def transaction_note(self, amount, type):
        self.transaction_history.append(f'user {self.note_translation[type]} ${amount}')
    def balance(self):
        return self.current_balance
    def check_withdrawal(self, amount):
        return self.current_balance - amount >= 0
    def deposit(self, amount):
        self.num_transactions += 1
        self.transaction_note(amount, 'deposit')
        self.current_balance += amount
    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.current_balance -= amount
            self.transaction_note(amount, 'withdraw')
            self.num_transactions += 1
            return amount
    def calc_interest(self):
        self.transaction_note(self.current_balance * self.interest_rate, 'interest')
        self.num_transactions += 1
        return self.current_balance * self.interest_rate
    def print_transactions(self, num):
        if num < self.num_transactions:
            for i in range(num):
                print(self.transaction_history[i])
        else:
            for line in self.transaction_history:
                print(line)

def validate_input(command):
    while command not in ['deposit', 'withdraw', 'balance', 'interest', 'history']:
        command = input('Invalid command, please try again.')
    return command

    




# test code
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history - transacton history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    elif command == 'history':
        num_entries = int(input('How many transactions previous to now would you like to review? '))
        atm.print_transactions(num_entries)
    else:
        print('Command not recognized')