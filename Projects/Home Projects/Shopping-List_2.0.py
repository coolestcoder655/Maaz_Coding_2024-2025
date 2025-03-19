# WAP to act as a shopping chat. It will have two lists. Item names and prices. Has to have: 

# Adding items with price
# Removing items
# Checking out
# Manager functionality
# Customer mode



# Functions
def findItemLoop(name):
    lname = name.casefold()
    for x in itemsInStore:
        if x[0] == lname:
            return itemsInStore.index(x)

def addItemToStore(name, price):
    itemsInStore.append((name, price))

def removeItemFromStore(name):
    item = findItemLoop(name)
    itemsInStore.pop(item)


def modifyPrice(name, newPrice):
    x = findItemLoop(name)
    unModifyed = list(x)
    unModifyed[1] = newPrice
    modifyed = tuple(unModifyed)
    indexToInsert = itemsInStore.index(x)
    itemsInStore.pop(indexToInsert)
    itemsInStore.insert(indexToInsert, modifyed)

def checkOut():
    total = []
    moneyTotal = 0
    for x in itemsInCustomerCart:
            for y in itemsInStore:
                if y[0] == x:
                    total.append(y[1])
    for z in total:
        moneyTotal = moneyTotal + z
    return moneyTotal

def removeItemFromCart(name):
    lname = name.casefold()
    for x in itemsInCustomerCart:
        if x == lname:
            itemsInCustomerCart.pop(itemsInCustomerCart.index(x))
# Variables
password = "qazwsxed"
itemsInStore = [
    ("bananas", 0.50, "b"),
    ("apples", 1.50, "i"),
    ("oranges", 1.25, "b"),
    ("tomatoes", 2.00, "i"),
    ("potatoes", 1.00, "i"),
    ("carrots", 1.50, "i"),
    ("lettuce", 2.00, "i"),
    ("broccoli", 2.50, "i"),
    ("spinach", 3.00, "i"),
    ("avacados", 2.00, "i")
]
itemsInCustomerCart = []
orangePrice = float(2.91)
bananasPrice = float(0.62)


while True:
    credentials = int(input("Welcome to Floormart!!! \n Are you a Manager or Customer?: \n 1 = Customer \n 2 = Manager \n 0 = End Program \n Input: "))

    if credentials == 1:
        customerChoice = int(input("Welcome New Customer. How May I Assist In Your Very Pricy Shopping? \n 1 = Add Item To Cart \n 2 = Remove Item From Cart \n 3 = Checkout \n Input: "))

        if customerChoice == 1:
            print("The Store Website Reads The Following Items Are In The Store: \n", itemsInStore)
            toAppend = (input("Please Enter The Item To Be Added To Your Cart:"))
            quantity = (int(input("Please Enter the Quantity Of The Item To Be Added: ")))
            itemsInCustomerCart.append(toAppend, quantity)
        elif customerChoice == 2:
            removeItemFromCart(input("Please Enter The Item To Be Removed From Your Cart:"))
        elif customerChoice == 3:
            print(checkOut())
        else:
            print("Please Enter A Value, Either 1, 2, 3.")
    elif credentials == 2:
        password2Check = input("Please Enter Your Password:")
        if password2Check == password or password2Check == "SecretCEOOveride":
            managerChoice = int(input("Welcome, Mr. Mister. How May I Assist In Your Chivalrous Affairs? \n 1 = Check Store Inventory \n 2 = Report New Item Shipment \n 3 = Report Removed Items \n 4 = Modify Item Price \n Input: ")) # Add Feature To See Items In Store / Add Modify Price
            if managerChoice == 1:
                print(itemsInStore)
            elif managerChoice == 2:
                itemToAdd = input("Please Enter The Name of The Item To Add:")
                priceOfItem = float(input("Please Enter The Price Of The Item To Add:"))
                addItemToStore(itemToAdd, priceOfItem)
            elif managerChoice == 3:
                itemtoRemove = input("Please Enter The Item To Be Removed:")
                removeItemFromStore(itemtoRemove)
            else:
                print("Please Enter A Value, Either 1 or 2.")
        else:
            print("Wrong Password. Please Enter Credentials Again.")
    elif credentials == 0:
        break
    else:
        print("Please Print A Value, Either 1 or 2.")