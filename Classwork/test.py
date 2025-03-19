itemsInStore = [
    ("bananas", 0.50),
    ("apples", 1.50),
    ("oranges", 1.25),
    ("tomatoes", 2.00),
    ("potatoes", 1.00),
    ("carrots", 1.50),
    ("lettuce", 2.00),
    ("broccoli", 2.50),
    ("spinach", 3.00),  
]
def findItemLoop(name):
    lname = name.casefold()
    for x in itemsInStore:
        if x[0] == lname:
            return itemsInStore.index(x)
def checkOut():
    total = []
    moneyTotal = 0
    for x in itemsInCustomerCart:
        y = findItemLoop(x)
        total.append(y[1])
    for z in total:
        moneyTotal = moneyTotal + z
    return moneyTotal
itemsInCustomerCart = ["apples", "oranges"]
# for x in itemsInCustomerCart:
#     y = findItemLoop(x)
#     print(y[1])
# checkOut()
print(findItemLoop("apples"))