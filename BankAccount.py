import random


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Client(Person):
    def __init__(self, first_name, last_name, account_number, balance):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def view_balance(self):
        return print(f'Your balance is: {self.balance}')
    
    def withdraw_balance(self, withdrawn_amount):
        if withdrawn_amount < self.balance:
            self.balance -= withdrawn_amount
            return print(f'You have withdrawn: {withdrawn_amount}')
        else:
            print("Insufficient funds!")

    def add_balance(self, added_amount):
        self.balance += added_amount
        return print(f'You have added: {added_amount}')
    
    def __str__(self):
        return f'Name: {self.first_name}, Account Number: {self.account_number}, Balance: {self.balance}'


# Prompt user for client attributes
def create_client():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = random.randint(5002220, 9000000)
    balance = 0
    # Create an object to store the client's information
    client_account = Client(first_name, last_name, account_number, balance)
    # Return the object
    return client_account


def start():
    print("Welcome to the Account Management System")
    print("Let's create your account")
    # Create a client object
    client = create_client()
    flow = 0
    print(client)
    while flow != 3:
        print("Options:")
        print("1) Add balance")
        print("2) Withdraw balance")
        print("3) Exit")
        option = int(input("Enter an option: "))
        
        if option == 1:
            added_balance = float(input("Enter the amount to add: "))
            client.add_balance(added_balance)
            client.view_balance()
        elif option == 2:
            withdrawn_balance = float(input("Enter the amount to withdraw: "))
            client.withdraw_balance(withdrawn_balance)
            client.view_balance()
        elif option == 3:
            flow = 3
        else:
            print("Invalid option. Please select a valid option from the menu.")
    
    print("See you later!")
start()
