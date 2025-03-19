class Account():
    def __init__(self, accNum: int, balance: int = 0):
        self.balance = balance
        self.accNum = accNum

    def debit(self, withdrawl: int) -> None:
        if withdrawl <= 0:
            print("Not Valid Withdrawl Amount!!!")
            return NotImplementedError

        self.balance -= withdrawl
        print("Money Withdrawn.")
    
    def credit(self, deposit: int) -> None:
        if deposit <= 0:
            print("Not Valid Deposit Amount!!!")
            return NotImplementedError

        self.balance += deposit
        print("Money Depositied.")
    
    def viewBalance(self) -> None:
        print(self.balance)

myAccount = Account(5840741, 100000)


myAccount.viewBalance()

input()

myAccount.debit(50)
myAccount.viewBalance()

input()

myAccount.credit(100)
myAccount.viewBalance()