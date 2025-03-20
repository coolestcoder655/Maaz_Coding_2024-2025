from json import load, dump

filePath = r"C:\Users\khokh\OneDrive\Documents\Maaz_Coding_2024-2025\Classwork\Exams\Exam 4\Inventory_Management_System\products.json"

def truncateFile() -> None:
    with open(filePath, "w") as file:
        file.write("")

def loadProducts() -> dict:
    with open(filePath, "r") as file:
        data = load(file)
        data = data["products"]
    return data

def saveProducts(data: dict = {}) -> None:
    truncateFile()
    with open(filePath, "w") as file:
        dump({"products": data}, file, indent=4)