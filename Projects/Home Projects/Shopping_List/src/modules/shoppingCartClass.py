from itemClass import Item, Store

class ShoppingCart():
    def __init__(self):
        self.items = []

    def addItem(self, item: Item):
        if Store.checkItem(item):
            self.items.append(item)
        else:
            print("Item not available in store.")

    def removeItem(self, item: Item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in cart.")
