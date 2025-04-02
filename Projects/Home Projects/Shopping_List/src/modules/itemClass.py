from typing import Optional

class Item():
    def __init__(self, name: str, price: float, weighted: bool, weight: Optional[float] = None):

        self.name = name
        self.price = price
        self.weighted = weighted
        self.weight = weight

        if self.weighted and self.weight is None:
            raise ValueError("Weight must be provided for weighted items.")

        

    def __repr__(self):
        return f"Item({self.name}, ${self.price}, Is Weighted: {self.weighted})"

    def __str__(self):
        return f"Item: {self.name}, Price: {self.price}"
        
    def checkOut(self):
        total = 0
        for item in self.items:
            if item.weighted:
                total += item.weight * item.price
            else:
                total += item.price
        
        return total
