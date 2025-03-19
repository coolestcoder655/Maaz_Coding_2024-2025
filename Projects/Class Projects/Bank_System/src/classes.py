from random import randint
from datetime import date

class Account():

    today = date.today()
    maintanceDay = today.replace(day=1)

    accounts = []
    
    def __init__ (self, balance: int = 0, accNum: int = None, pin: int = None):
        self.balance = balance
        self.accNum = accNum if accNum is not None else int("".join([str(randint(1, 9)) for _ in range(8)]))
        self.pin = pin if pin is not None else int("".join([str(randint(1, 9)) for _ in range(4)]))
        self.isNegative = lambda: True if self.balance < 0 else False
        Account.accounts.append(self)
        self.loans = []


    def checkAccount(self) -> bool:
        if self in Account.accounts:
            return True
        else:
            return False
        
    def createAccount(self):
        try:
            if self.checkAccount():
                raise Exception("Account Already Exists")
            else:
                Account.accounts.append(self)
        except Exception as e:
            print("Account Already Exists: ", e)
    
    def credit(self, money: int):
        try:
            if self.checkAccount():
                self.balance += money
            else:
                raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)
        
    def debit(self, money: int):
        try:
            if self.checkAccount():
                self.balance -= money
            else:
                raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)

    def checkBalance(self) -> int:
        try:
            if self.checkAccount():
                return self.balance
            else:
                raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)

    def findAccount(self, accNum: int):
        try:
            for account in Account.accounts:
                if account.accNum == accNum:
                    return account
            raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)
        """
    def makeLoan(self, money: int):
        try:
            if self.checkAccount():
                if money < (self.balance / 2):
                    self.balance += money
                else:
                    raise ValueError("Loan Too High")
            else:
                raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)
        except ValueError as e:
            print("Loan Too High: ", e)
        """
    def signUpForCreditCard(self):
        try:
            if self.checkAccount():
                name = input("Please Enter First And Last Name To Complete Credit Card Sign Up: ")
                if name != " " or name != "":
                    print("Credit Card Sign Up Complete.")
                else:
                    raise ValueError("Name Not Entered")
            else:
                raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)
        except ValueError as e:
            print("Name Not Entered: ", e)


    @classmethod
    def findAccount(cls, accNum):
        try:
            for account in Account.accounts:
                if account.accNum == accNum:
                    return account
            raise Exception("Account Does Not Exist")
        except Exception as e:
            print("Account Does Not Exist; Please Create One: ", e)
            return NotImplementedError
        
    def createLoan(self):
        year = int(input("What Year?: "))
        month = int(input("What Month?: "))
        day = int(input("What Day?: "))
        newDate = date(year=year, month=month, day=day)

        money = int(input("How Much?: $"))

        newLoan = Loan(self, newDate, money, 10)
        return newLoan
    

    @classmethod
    def makeMaintance(cls, money):
        for account in cls.accounts:
            account.balance -= money
        print("Maintance Complete.")


class CurrencyConverter:
    conversion_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 74.0,
        'AUD': 1.35,
        'CAD': 1.25,
        'SGD': 1.36,
        'CHF': 0.92,
        'MYR': 4.15,
        'JPY': 110.0,
        'CNY': 6.45
    }

    @classmethod
    def convert(cls, amount: float, to_currency: str) -> float:
        try:
            if to_currency not in cls.conversion_rates:
                raise ValueError("Currency not supported")
            amount_in_usd = amount / cls.conversion_rates["USD"]
            return amount_in_usd * cls.conversion_rates[to_currency]
        except ValueError as e:
            print("Currency not supported: ", e)

class Loan():
    def __init__(self, account, date: date = date.today(), requestedMoney: int = 0, intrestRate: float = 10):
        self.date = date
        self.requestedMoney = requestedMoney
        self.intrestRate = intrestRate
        self.intrestInDollars = (requestedMoney * intrestRate * date.year) / 100
        self.account = account
        self.years = date.year()
    # amount * rate * years / 100

    def payBackOnTime(self):
        self.account.balance -= ((self.requestedMoney * self.intrestRate * self.date.year) / 100) + self.requestedMoney
        return self.account.balance

newAccount = Account(100)
print(Account.accounts)