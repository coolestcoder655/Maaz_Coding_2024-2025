class Account:
    def __init__(self, balance: int):
        self.balance = balance
    
    def credit(self, money):
        self.balance += money
        return self.balance
    def debit(self, money):
        self.balance -= money
        return self.balance
    def __str__(self):
        return f"Balance: ${self.balance}"
    def __repr__(self):
        return self.balance
    
myAccount = Account(100)
print(myAccount.credit(100))
print(myAccount.debit(50))
print(myAccount.__str__())
print(myAccount.__repr__())