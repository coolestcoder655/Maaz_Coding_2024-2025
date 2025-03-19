# **The *Sterling Reserve Bank* Management Platform**

This project is a comprehensive banking system designed to manage user accounts with various functionalities such as creating accounts, crediting and debiting money, checking balances, making loans, signing up for credit cards, and performing maintenance tasks.

## 📁 File Structure

```plaintext
Bank_System/
    ├── src/
    │   ├── __pycache__/
    │   │   ├── classes.cpython-311.pyc
    │   │   └── state.cpython-311.pyc
    │   ├── classes.py
    │   ├── main.py
    │   └── state.py
    └── README.md
```

## ✨ Features

- **Create an Account**: Initialize an account with an initial balance and a random account number.
- **Credit Money**: Add funds to an account.
- **Debit Money**: Withdraw funds from an account.
- **Check Balance**: View the current balance of an account.
- **Customer Management**: Maintain a list of up to 5 customers.
- **Account Access**: Create an account or log in.
- **Loan Management**: Apply for a loan (loan amount must be lower than 50% of the balance).
- **Credit Card Signup**: Register for a credit card.
- **Maintenance**: Perform maintenance on the first day of every month (manual/auto).

## 🏦 Classes

### `Account`

The `Account` class represents a bank account and provides methods to perform various operations.

#### Methods

- `__init__(self, balance: int = 0, accNum: int = None, pin: int = None)`: Initializes a new account with a balance, a random account number, and a random pin.
- `checkAccount(self) -> bool`: Checks if the account exists.
- `createAccount(self)`: Creates a new account.
- `credit(self, money: int)`: Credits money to the account.
- `debit(self, money: int)`: Debits money from the account.
- `checkBalance(self) -> int`: Checks the balance of the account.
- `findAccount(self, accNum: int)`: Finds an account by account number.
- `makeLoan(self, money: int)`: Makes a loan (loan amount must be lower than 50% of the balance).
- `signUpForCreditCard(self)`: Signs up for a credit card.
- `makeMaintance(cls, money)`: Performs maintenance by deducting a specified amount from all accounts.

## 🚀 Usage

To use the bank system, create instances of the `Account` class and call the methods to perform various operations.

```python
from classes import Account

# Create new accounts
newAccount1 = Account(1584.32)
newAccount2 = Account(2584.32)
newAccount3 = Account(3584.32)
newAccount4 = Account(4584.32)
newAccount5 = Account(5584.32)

# Perform operations
newAccount1.credit(100)
newAccount2.debit(50)
balance = newAccount3.checkBalance()
newAccount4.makeLoan(200)
newAccount5.signUpForCreditCard()
```

## 📝 Script Overview

The main script [`main.py`](src/main.py) initializes the bank system and provides a command-line interface for users to interact with the system.

The [`classes.py`](src/classes.py) contains the `Account` class and its methods, which are used to manage the bank accounts and perform various operations such as creating accounts, crediting and debiting money, checking balances, making loans, and signing up for credit cards.

The state file [`state.py`](src/state.py) manages the state of the bank system and directs the [`main.py`](src/main.py) file during its operation.

## 🛠️ How to Run

You can run the bank management system in two simple steps:

1. **Navigate to the Source Directory**

    Open PowerShell and change the directory to the `src` folder of the project. Replace `pathToTheFile` with the actual path to the `src` folder.

    ```powershell
    cd "pathToTheFile"
    ```

2. **Execute the Main Script**

    Run the following command to start the bank management system:

    ```powershell
    python main.py
    ```

### Running a Python File Using the Complete Path

If you prefer not to navigate to the file's directory, you can run the Python script directly by providing its full path. Simply replace the path in the quotation marks with the actual location of your Python file.

```powershell
python "C:\Users\YourUsername\path\to\your\file\filename.py"
```