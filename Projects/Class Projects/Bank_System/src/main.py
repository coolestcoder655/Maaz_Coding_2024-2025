# Bank With Customers

# Create An Account: Inital = 0, AccNum = anything ✅

# Credit: if no accoun: NO ERROR ✅

# Debit: no account, No ERROR ✅

# checkBalance ✅

# Mantain 5 customers ✅

# Create Acc or Login ✅

# Make A Loan: loan is lower than 50% balance ✅

# Sign For Credit Card ✅
# First day of every month, manual/auto ✅

from sys import path
path.append(r"Bank_System\\src\\")
from os import system
from classes import Account, CurrencyConverter
from state import State


newAccount1 = Account(balance=1584.32, pin=1234, accNum=10000001)
newAccount2 = Account(balance=2584.32, pin=4321, accNum=10000002)
newAccount3 = Account(balance=3584.32, pin=5678, accNum=10000003)
newAccount4 = Account(balance=4584.32, pin=8765, accNum=10000004)
newAccount5 = Account(balance=5584.32, pin=9876, accNum=10000005)

def clearOutput():
    system("cls")

# Initization
state = State.MainMenu
running = True

while running:
    clearOutput()
    if Account.today == Account.maintanceDay:
        Account.makeMaintance(100)
    
    if state == State.MainMenu:                                                             # Main Menu
        while True:
            print("1. Create Account")
            print("2. Login")
            print("0. Exit")
            choice = int(input("Enter Choice: "))
            if choice == 1:
                state = State.CreateAccount
                break
            elif choice == 2:
                state = State.Login
                break
            elif choice == 0:
                print("Exiting...")
                running = False
                break
            else:
                print("Invalid Choice. Try Again.")
            clearOutput()
    elif state == State.CreateAccount:                                                      # Create Account
        print("Creating Account...")
        balance = float(input("Enter Initial Balance: "))
        newAccount = Account(balance)
        print(f"Account Created, Your Account Number Is: '{newAccount.accNum}' and Your Pin Is: '{newAccount.pin}.' Please Press Enter To Continue.")
        input()
        state = State.Login
    elif state == State.Login:                                                              # Login
        accNum = int(input("Enter Account Number: "))
        account = Account.findAccount(accNum=accNum)
        if account == NotImplementedError:
            state = State.CreateAccount
            continue
        pin = int(input("Enter Pin: ")) 
        if account.pin == pin:
            state = State.AccountScreen
        else:
            print("Invalid Account Number Or Pin.") 
    elif state == State.AccountScreen:
        while True:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Make Loan")
                print("4. Sign Credit Card")
                print("5. Maintenance")
                print("6. Change PIN")
                print("7. Currency Converter")
                print("0. Exit")

                print(f"\n Balance: ${account.checkBalance()} \n")
                choice = int(input("Enter Choice: "))
                if choice == 1:
                    money = float(input("Enter Amount To Deposit: "))
                    account.credit(money)
                elif choice == 2:
                    money = float(input("Enter Amount To Withdraw: "))
                    account.debit(money)
                elif choice == 3:
                    money = float(input("Enter Amount To Loan: "))
                    account.makeLoan(money)
                elif choice == 4:
                    account.signUpForCreditCard()
                elif choice == 5:
                    money = int(input("Enter Amount For Maintenance: "))
                    Account.makeMaintance(money)
                elif choice == 6:
                    newPin = int(input("Enter New Pin: "))
                    account.pin = newPin
                elif choice == 7:
                    clearOutput()
                    for index, currency in enumerate(CurrencyConverter.conversion_rates.keys()):
                        print(f"{index}. USD to {currency}: 1.0 = {CurrencyConverter.conversion_rates[currency]}")
                    currency = int(input("Enter Choice: "))
                    if currency == 0:
                        print("Cannot Convert USD to USD.")
                        continue
                    elif currency == 1:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: €{CurrencyConverter.convert(money, 'EUR')}")
                    elif currency == 2:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: £{CurrencyConverter.convert(money, 'GBP')}")
                    elif currency == 3:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: ₹{CurrencyConverter.convert(money, 'INR')}")
                    elif currency == 4:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: ${CurrencyConverter.convert(money, 'AUD')}")
                    elif currency == 5:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: ${CurrencyConverter.convert(money, 'CAD')}")
                    elif currency == 6:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: ${CurrencyConverter.convert(money, 'SGD')}")
                    elif currency == 7:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: ₣{CurrencyConverter.convert(money, 'CHF')}")
                    elif currency == 8:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: RM{CurrencyConverter.convert(money, 'MYR')}")
                    elif currency == 9:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: ¥{CurrencyConverter.convert(money, 'JPY')}")
                    elif currency == 10:
                        money = float(input("Enter Amount To Convert: "))
                        print(f"Converted Amount: CN¥{CurrencyConverter.convert(money, 'CNY')}")
                    input("Press Enter To Continue.")

                elif choice == 0:
                    state = State.MainMenu
                    break
                else:
                    print("Invalid Choice. Try Again.")
                clearOutput()
        