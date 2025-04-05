from dataclasses import dataclass
from utilites import ChangeToInt


@dataclass
class Product():
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price Cannot Be Negative")
        if self.quantity < 0:
            raise ValueError("Quantity Cannot Be Negative")
        if not isinstance(self.name, str):
            raise TypeError("Name must be a string")
        
        self.price = ChangeToInt(self.price)
        

def test_product():
    # Test valid product
    product = Product(name="Test Product", price=10.0, quantity=5)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 5

    # Test negative price
    try:
        Product(name="Test Product", price=-10.0, quantity=5)
    except ValueError as e:
        assert str(e) == "Price Cannot Be Negative"

    # Test negative quantity
    try:
        Product(name="Test Product", price=10.0, quantity=-5)
    except ValueError as e:
        assert str(e) == "Quantity Cannot Be Negative"

    # Test invalid name type
    try:
        Product(name=123, price=10.0, quantity=5)
    except TypeError as e:
        assert str(e) == "Name must be a string"


test_product()