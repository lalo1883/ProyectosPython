# Bank Account Management System

This is a simple Python script that simulates a bank account management system. The script defines a `Person` class and a `Client` class that inherits from the `Person` class. Methods are implemented to interact with client accounts, such as viewing balance, adding balance, and withdrawing balance.

## Usage

1. Run the script in your Python environment.
2. The program will welcome you and ask you to enter your details to create a new client account.
3. After creating the account, you can choose from several options to interact with the account:
   - **Add balance**: Enter an amount of money to increase the account balance.
   - **Withdraw balance**: Enter an amount of money to withdraw from the account balance, if there's sufficient balance available.
   - **Exit**: End the interaction and terminate the program.

## Classes and Methods

### `Person` Class

This class defines a person with attributes of a first name and a last name.

### `Client` Class

This class inherits from the `Person` class and represents a bank client. Clients have additional attributes like account number and balance. Methods available for objects of this class are:

- `view_balance()`: Displays the current account balance.
- `withdraw_balance(withdrawn_amount)`: Withdraws a specified amount from the account balance, if there's sufficient balance available.
- `add_balance(added_amount)`: Adds a specified amount to the account balance.
- `__str__()`: Returns a string representation of the client.

### Functions

- `create_client()`: Prompts the user to enter their first name and last name, then creates a `Client` object with a random account number and an initial balance of 0.
- `start()`: Initiates user interaction. Allows the user to select options to add balance, withdraw balance, or exit the program.

## Example Usage

1. Run the script.
2. Enter your first name and last name when prompted.
3. Your client account will be created with a random account number and an initial balance of 0.
4. A menu with options to add balance, withdraw balance, or exit the program will be displayed. Follow the on-screen instructions to interact with the account.

**Note:** This script is a simple simulation and does not reflect a real banking security implementation. It's not recommended to use this script for production purposes.
