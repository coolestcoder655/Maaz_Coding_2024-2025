# Restaurant Order System

A Python-based Restaurant Order Management System that allows restaurants to manage customer orders efficiently. This system supports creating new orders, adding items to orders, removing items, calculating the total price, and viewing the details of all current orders.

---

## Features

- Create new orders with a unique `Order ID` and `Table Number`.
- Add or remove items from an order with proper validation to avoid duplicates.
- Calculate the total price of an order.
- Display the details of all current orders in a readable format.
- Utility functions to clear the console and ensure proper data types.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <REPOSITORY_URL>
   ```
2. Navigate to the project directory:
   ```powershell
   cd "Path\To\The\File"
   ```
3. Ensure that you have **Python 3.9+** installed:
   ```powershell
   python --version
   ```
4. Install required dependencies:
   ```powershell
   pip install colorama
   ```

## Usage

To interact with the **Restaurant Order System**, simply run the `main.py` file. The file currently provides a CLI (Command Line Interface) for interacting with orders.

### Steps

1. Run the application:
   ```bash
   python src/main.py
   ```
2. Follow the on-screen instructions to:
   - Create a new order.
   - Add, view, or remove items in the order.
   - Calculate the total price of an order.

---

## Code Overview

### `classes.py`

Contains the `Restaurant` class, which encapsulates the core logic for managing restaurant orders.

- `createNewOrder(orderID, tableNumber)`  
  Creates a new order with a unique order ID and table number.

- `findOrder(orderID)`  
  Finds and retrieves an order using the order ID.

- `addNewItem(orderID, itemName, itemPrice)`  
  Adds a new item to an existing order.

- `removeItem(orderID, itemName)`  
  Removes an item by name from an existing order.

- `calculateTotalPrice(orderID)`  
  Calculates the total price of all items in a given order.

- `viewOrder()`  
  Prints details of all orders, including the order IDs, table numbers, and the list of items and their prices.

### `utilites.py`

Provides utility functions to clear the console and manage data types.

- `clearScreen()`  
  Clears the terminal or console.

- `turnIntoInt(num)`  
  Converts a float to an integer if it has no decimal part.

### `main.py`

The entry point of the project. This script provides a user interface (primarily a CLI) to interact with the features of the restaurant order system.

---

## Utilizing this program

```python
from classes import Resturant   # Import This Directory

obj = Resturant()

obj.createNewOrder(orderID=1, tableNumber=1)

obj.addNewItem(orderID=1, itemName="Pizza", itemPrice=29.69)

print(obj.calculateTotalPrice(orderID=1))

```