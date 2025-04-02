from modules.itemClass import Item
from modules.storeClass import Store
from modules.shoppingCartClass import ShoppingCart
from modules.fileManager import readItems, writeItems

def main() -> None:
    store = Store()



    print("Welcome To Floormart.")
    print("1. Customer")
    print("2. Manager")
    print("0. Exit")
    choice = input("Enter your choice: ")


if __name__ == "__main__":
    main()