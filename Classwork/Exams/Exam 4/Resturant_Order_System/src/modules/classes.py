from random import randint
from uuid import uuid4

class Restaurant:
    def __init__(self, orders = None) -> None:
        if orders is None:
            orders = []

        self.orders = orders    # {orderID, tableNumber, orderList}
    
    def findOrder(self, orderID: int):
        for order in self.orders:
            if order["orderID"] == orderID:
                return order
        raise Exception("Order not found.")

    def createNewOrder(self, orderID: int | None, tableNumber: int | None):
        if orderID is None:
            orderID = int(f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}")

        if tableNumber is None:
            tableNumber = randint(1, 9)


        if any([tableNumber == x['tableNumber'] or orderID == x['orderID'] for x in self.orders]):
            raise Exception("Order already exists")

        newOrder = {
            "orderID": orderID,
            "tableNumber": tableNumber,
            "orderList": []
        }
        self.orders.append(newOrder)

    def addNewItem(self, orderID: int, itemName: str, itemPrice: float):
        if any([itemName == x for x in self.orders]):
            raise Exception("Cannot Add Duplicate Item.")

        order = self.findOrder(orderID)
        order["orderList"].append({"itemName": itemName, "itemPrice": itemPrice})
        
    def removeItem(self, orderID: int, itemName: str):
        order = self.findOrder(orderID)

        for item in order["orderList"]:
            if item["itemName"] == itemName:
                order["orderList"].remove(item)
                return
        raise Exception("Item not found.")

    def calculateTotalPrice(self, orderID: int):
        prices = []
        order = self.findOrder(orderID)

        for item in order["orderList"]:
            prices.append(item["itemPrice"])

        return f"{sum(prices):.2f}"

    def viewOrder(self):
        for orderIndex, order in enumerate(self.orders):
            print(f"Order {orderIndex + 1}:")
            print(f"Order ID: {order['orderID']}")
            print(f"Table Number: {order['tableNumber']}")
            for index, item in enumerate(order["orderList"]):
                print(f"     {index + 1}. {item['itemName']}: ${item['itemPrice']}")