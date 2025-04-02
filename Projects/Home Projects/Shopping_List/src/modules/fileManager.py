from json import load, dump
from itemClass import Item

filePath = r"data\items.json"

def loadItems() -> list[Item]:
    try:
        with open(filePath, "r") as file:
            items = load(file)
            for item in items:
                Item(name=item["name"], price=item["price"], weighted=item["weighted"], weight=item["weight"])
    except:
        raise Exception("Error Loading Items, Contact Dev For Support")