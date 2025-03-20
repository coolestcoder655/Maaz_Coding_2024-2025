from classes import Inventory
from fileManagement import saveProducts, loadProducts
from colorama import Fore, Style, Back, init
from os import system

def clearOutput() -> None:
    system("cls")

init(autoreset=True)


def askForInt(prompt: str = "Please Enter Your Choice: ") -> int:
    while True:
        try:
            num = int(input(prompt))
        except ValueError as v:
            print("Input Has To Be A Number: {}", v)
        else:
            return num
        
def askForFloat(prompt: str = "Please Enter Your Choice: ") -> float:
    while True:
        try:
            num = float(input(prompt))
        except ValueError as v:
            print("Input Has To Be A Number: {}", v)
        else:
            return num


inventory = Inventory(loadProducts())

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.BLACK, Fore.RESET]
styles = [Style.BRIGHT, Style.NORMAL, Style.DIM]

try:
    while True:
        clearOutput()

        print(colors[5] + styles[0] + "Welcome To The Inventory Management System!")
        print(colors[5] + styles[0] + "===========================================")

        print(styles[0] + "\nWhat Would You Like To Do?: \n ")

        print(colors[0] + styles[0] + "1. Add A Product.")
        print(colors[1] + styles[0] + "2. Update A Product.")
        print(colors[2] + styles[0] + "3. Remove A Product.")
        print(colors[3] + styles[0] + "4. Calculate Total Inventory Value.")
        print(colors[4] + styles[0] + "5. Add Quantites Together.")
        print(colors[5] + styles[0] + "6. View All Products In Inventory.")
        print(Back.RED + styles[0] + "0. Exit." + Back.RESET + "\n")

        userChoice = askForInt()

        if userChoice == 1:
            newName = input("Please Enter The Name Of The Product: ")
            newPrice = askForFloat("Please Enter The Price Of The Item: ")
            newQuantity = askForInt("Please Enter The Quantity Of The Item: ")

            inventory.addProduct(newName, newPrice, newQuantity)
        elif userChoice == 2:

            newName = input("Please Enter The Name Of The Product To Modify: ")

            while True:
                editPriceChoice = input("Change Price?: (y/n) ")
                editPriceChoice = editPriceChoice.upper()

                if editPriceChoice == "Y":
                    editPrice = True
                    break
                elif editPriceChoice == "N":
                    editPrice = False
                    break
                else:
                    print("Invalid Input Type, Restarting...")

            while True:


                editQuantityChoice = input("Change Quantity?: (y/n) ")
                editQuantityChoice = editQuantityChoice.upper()

                if editQuantityChoice == "Y":
                    editQuantity = True
                    break
                elif editQuantityChoice == "N":
                    editQuantity = False
                    break
                else:
                    print("Invalid Input Type, Restarting...")

            if editPrice == True:
                editPrice = askForFloat("Please Enter The New Price: ")

            if editQuantity == True:
                editQuantity = askForInt("Please Enter The New Quantity: ")

            inventory.updateProduct(
                newName,
                editPrice if editPrice else print("", end=""),
                editQuantity if editQuantity else print("", end="")
            )

        elif userChoice == 3:
            newName = input("Please Enter The Name Of The Product To Delete: ")

            inventory.removeProduct(newName)

        elif userChoice == 4:
            inventory.calculateTotalValue()

        elif userChoice == 5:
            newName = input("Please Enter The Name Of The Product To Add To: ")
            newQuantity = askForInt("Please Enter The Added Quantity: ")

            inventory = inventory + (newName, newQuantity)

        elif userChoice == 6:
            print(inventory.__str__())

        elif userChoice == 0:
            break

        input("Press Enter To Continue...")
except KeyboardInterrupt:
    print("Forced Keyboard Quit: Exiting...") 
    
    
    
del inventory