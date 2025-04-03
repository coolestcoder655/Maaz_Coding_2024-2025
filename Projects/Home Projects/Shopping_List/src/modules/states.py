from enum import Enum

class State(Enum):
    Login = 0
    MainMenu = 1
    AddItem = 2
    RemoveItem = 3
    ViewItems = 4
    Checkout = 5
    Exit = 0