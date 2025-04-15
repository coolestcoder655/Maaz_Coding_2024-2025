from fileManagement import saveProducts

class Inventory():
    def __init__(self, products: dict = {}):
        self.products = products

    def __add__(self, parameters: tuple = ()):
        name = parameters[0]
        quantity = parameters[1]
        self.products[name] = {
            "price": self.products[name].get("price"),
            "quantity": (self.products[name].get("quantity") + quantity)
        }

    def __del__(self):
        saveProducts(self.products)

    def __str__(self):
        for value, item in enumerate(self.products.keys()):
            value += 1

            print(f"{value}. {item}:")
            print(f"  Price: ${self.products[item].get("price"):.2f}")
            print(f"  Quantity: {self.products[item].get("quantity")}\n")


    def addProduct(self, name: str = "untitled product", price: float = 0, quantity: int = 0) -> dict:
        if any(name in item for item in self.products.keys()):
            print(f"Product \"{name}\" already exists in inventory.")
            print("Would you like to add new quantity to existing product? (y/n)")
            editQuantity = input().lower()
            if editQuantity == "y":
                self.products[name]["quantity"] += quantity
            else:
                print("No changes made.")
        else:
            self.products[name] = {
                    "price": price,
                    "quantity": quantity
                }
        
        return self.products
        
    def removeProduct(self, name: str) -> dict:
        self.products.pop(name)
        return self.products

    def updateProduct(self, name: str, **kwargs): # price=100, quantity=50
        if "price" in kwargs.keys():
            price = kwargs.get("price", None)
        else:
            price = None
        if "quantity" in kwargs.keys():
            quantity = kwargs.get("quantity", None)
        else:
            quantity = None
        
        product = self.products.get(name, None)
        product["quantity"]


        self.products[name] = {
            "price": price if price is not None else product["price"],
            "quantity": quantity if quantity is not None else quantity["quantity"]
        }

    def calculateTotalValue(self):
        for item in self.products.values():
            price = item.get("price", "NaN")
            quantity = item.get("quantity", "NaN")
            print(f"{item}: ${price} * {quantity} = ${price * quantity}")