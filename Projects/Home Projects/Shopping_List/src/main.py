from modules.itemClass import Item
from modules.storeClass import Store
from modules.shoppingCartClass import ShoppingCart
from modules.fileManager import readItems, writeItems
from modules.states import State

def main() -> None:
    store = Store(items=readItems())
    cart = ShoppingCart()
    currentState = State.Login

    while True:
        print("Welcome To Floormart.")
        print("1. Customer")
        print("2. Manager")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":


if __name__ == "__main__":
    main()