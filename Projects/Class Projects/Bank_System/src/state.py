from enum import Enum

class State(Enum):
    MainMenu = 0
    CreateAccount = 1
    Login = 2
    Deposit = 3
    Withdraw = 4
    CheckBalance = 5
    MakeLoan = 6
    SignCreditCard = 7
    Maintenance = 8
    AccountScreen = 9