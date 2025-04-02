from itemClass import Item

class Store():
    def __init__(self, items: list[Item] = []):
        self.items = items

    def addItem(self, item: Item):
        self.items.append(item)
    
    def removeItem(self, item: Item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in store.")
    
    def checkItem(self, item: Item) -> bool:
        return item in self.items
    
    def __repr__(self):
        return f"Store({self.items})"
    
    def __str__(self):
        return f"Store: {', '.join([item.name for item in self.items])}"