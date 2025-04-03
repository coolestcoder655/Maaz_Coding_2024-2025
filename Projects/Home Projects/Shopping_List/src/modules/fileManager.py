from json import load, dump, JSONDecodeError
from itemClass import Item

filePath = r"data\items.json"

def loadItems() -> list[Item]:
    Store = list()
    try:
        with open(filePath, "r") as file:
            items = load(file)
            for item in items:
                Store.append(Item(name=item["name"], price=item["price"], weighted=item["weighted"], weight=item["weight"]))
            return Store
    except FileNotFoundError:
        raise FileNotFoundError("File Not Found, Contact Dev For Support")
    except JSONDecodeError:
        raise ValueError("File is not a valid JSON, Contact Dev For Support")
    
    except:
        raise Exception("Error Loading Items, Contact Dev For Support")