from modules.classes import Restaurant
from modules.utilites import clearScreen
from colorama import Style, Fore, Back, init

styles = [Style.BRIGHT, Style.NORMAL, Style.DIM]
fores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.BLACK]

init(autoreset=True)

def main() -> None:
    obj = Restaurant()

    clearScreen()

    print(styles[0] + fores[1] + "Welcome To The Restaurant Order System.")
    print(styles[0] + fores[1] + "---------------------------------------")

    try:
        while True:
            print("What would you like to do?")
            print(fores[0] + "1. Create New Order.")
            print(fores[1] + "2. Order Item.")
            print(fores[2] + "3. Remove Item.")
            print(fores[3] + "4. View Order.")
            print(fores[4] + "5. Print Total Cost Of Order.")
            print(fores[5] + Back.RED + "Press Ctrl + C To Exit AT ANY TIME.")

            choice = input("Enter your choice: ")
            if choice == "1":
                orderNumber = input("Enter your order number; leave blank for random: ")
                tableNumber = input("Enter your table number; leave blank for random: ")

                if orderNumber.strip() == "":
                    orderNumber = None
                else:
                    try:
                        orderNumber = int(orderNumber)  # Explicitly convert to int
                    except ValueError:
                        print(fores[0] + "Order number must be an integer.")
                        continue  # Retry user input

                if tableNumber.strip() == "":
                    tableNumber = None
                else:
                    try:
                        tableNumber = int(tableNumber)  # Explicitly convert to int
                    except ValueError:
                        print(fores[0] + "Table number must be an integer.")
                        continue  # Retry user input

                try:
                    obj.createNewOrder(orderNumber, tableNumber)
                except Exception as e:
                    print(e)



            elif choice == "2":
                orderNumber = None
                itemPrice = None

                while True:
                    try:
                        orderNumber = int(input("Enter the order number: "))  # Ensure int input
                    except ValueError:
                        print(fores[0] + "Invalid number. Please try again.")
                        continue
                    else:
                        break

                itemName = input("Enter the item name: ")

                while True:
                    try:
                        itemPrice = float(input("Enter the item price: "))  # Ensure float input
                    except ValueError:
                        print(fores[0] + "Invalid price. Please try again.")
                        continue
                    else:
                        break

                try:
                    obj.addNewItem(orderID=orderNumber, itemName=itemName, itemPrice=itemPrice)
                except Exception as e:
                    print(e)

            elif choice == "3":
                orderNumber = input("Enter your order number: ")
                itemName = input("Enter the item name: ")

                try:
                    obj.removeItem(orderID=int(orderNumber), itemName=itemName)    # Add Error Handing To All | NOT FINISHED
                except Exception as e:
                    print(e)

            elif choice == "4":
                obj.viewOrder()

            elif choice == "5":
                orderNumber = None

                while True:
                    try:
                        orderNumber = int(input("Please enter the order number: "))
                    except ValueError:
                        print(fores[0] + "Invalid number. Please try again.")
                        continue
                    else:
                        break

                print(obj.calculateTotalPrice(orderID=orderNumber))

            input(styles[0] + fores[1] + "Press Enter To Continue...")
            clearScreen()
    except KeyboardInterrupt:
        print(styles[0] + fores[1] + "Exiting...")

if __name__ == '__main__':
    main()