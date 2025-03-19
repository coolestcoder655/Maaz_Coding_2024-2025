# Inventory Management System

This project is an Inventory Management System that allows users to manage products, including adding, updating, removing, and viewing products. It also calculates the total inventory value.

## File Structure

```
Inventory_Management_System/
│
├── classes.py
├── fileManagement.py
├── main.py
├── products.json
└── README.md
```

### `classes.py`

This file contains the `Inventory` class, which manages the inventory of products. It includes methods for adding, updating, removing products, and calculating the total inventory value.

### `fileManagement.py`

This file contains functions for loading and saving products to a JSON file. It includes:
- `truncateFile()`: Clears the contents of the JSON file.
- `loadProducts()`: Loads products from the JSON file.
- `saveProducts(data)`: Saves products to the JSON file.

### `main.py`

This is the main entry point of the application. It provides a command-line interface for interacting with the inventory. It includes options for adding, updating, removing products, calculating total inventory value, and viewing all products.

### `products.json`

This file contains the initial data for the products in the inventory. It is used to load and save product data.

### `README.md`

This file provides an overview of the project, including the file structure and brief descriptions of each file.

## How to Import and Run the Project

1. **Navigate to the project directory:**
    ```powershell
    cd "C:/PathToTheFile/Inventory_Management_System/src"
    ```

2. **Install the required dependencies:**
    ```powershell
    pip install colorama
    ```

3. **Run the main script:**
    ```powershell
    python main.py
    ```

This will start the Inventory Management System, and you can interact with it through the command-line interface.
