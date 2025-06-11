# Part A – User Info
# Collect name and delivery address using Entry widgets. ✅
# Part B – Product Selection
# Use Checkbuttons to select items:
# Milk ($2) ✅
# Bread ($1.5) ✅
# Eggs ($3) ✅
# Fruits ($4) ✅
# Part C – Quantity
# Add an Entry next to each item to allow quantity selection (only enabled if item is selected). ✅
# Part D – Bill Calculation
# On clicking “Checkout”, calculate and show total in a Label. ✅
# Use messagebox.askyesno() to confirm the order.
# On “Yes”, show a thank you message.

import tkinter as tk
from tkinter.messagebox import askyesno, showinfo  # type: ignore

from typing import Any
from json import dump


root = tk.Tk()
root.title('Food Delivery App')
root.geometry('300x425')

from typing import Any

def makeInt(num: float) -> float | int:
    if int(num) == num:
        return int(num)
    else:
        return num

def checkout() -> None:
    global nameEntry, addressEntry, milk, eggs, bread, fruits

    menu: dict[str, float] = {
        'milk': 2.0,
        'bread': 1.5,
        'eggs': 3.0,
        'fruits': 4.0
    }

    total: float = 0.0

    isMilk = milk.get()
    isEggs = eggs.get()
    isBread = bread.get()
    isFruits = fruits.get()
    name = nameEntry.get()
    address = addressEntry.get()

    try:
        milk_qty = int(milkQuantity.get()) if isMilk else 0
    except ValueError:
        milk_qty = 0
    try:
        bread_qty = int(breadQuantity.get()) if isBread else 0
    except ValueError:
        bread_qty = 0
    try:
        eggs_qty = int(eggsQuantity.get()) if isEggs else 0
    except ValueError:
        eggs_qty = 0
    try:
        fruits_qty = int(fruitsQuantity.get()) if isFruits else 0
    except ValueError:
        fruits_qty = 0

    total += milk_qty * menu['milk']
    total += bread_qty * menu['bread']
    total += eggs_qty * menu['eggs']
    total += fruits_qty * menu['fruits']
    confirm = askyesno(title='Confirm Order', message=f'Would you like to confirm this order?\nTotal: {total}')
    if confirm:
        showinfo(title='Order Placed', message='Your order has been placed. Thank you!')
        receipt: dict[str, Any] = {
            'name': name,
            'address': address,
            'total': total,
        }
        with open('receipt.json', 'w') as file:
            dump(receipt, file)

# Name + Address
tk.Label(root, text='Name:').grid(column=0, row=1)
nameEntry = tk.Entry(root)
nameEntry.grid(column=0, row=2)

tk.Label(root, text='Address:').grid(column=0, row=3)
addressEntry = tk.Entry(root)
addressEntry.grid(column=0, row=4)

def toggleInput(entry: tk.Entry, label: tk.Label, variable: tk.BooleanVar, row: int):
    if variable.get():
        label.grid(column=0, row=row + 1)
        entry.grid(column=0, row=row + 1)
    else:
        label.grid_forget()
        entry.grid_forget()

# Product Selection
milk = tk.BooleanVar(value=False)
bread = tk.BooleanVar(value=False)
eggs = tk.BooleanVar(value=False)
fruits = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Milk ($2)", command=lambda: toggleInput(milkQuantity, milkLabel,  milk, 6), variable=milk).grid(column=0, row=5)
milkLabel =  tk.Label(root, text='How Much?:')
milkQuantity = tk.Entry(root)

tk.Checkbutton(root, text="Bread ($1.50)", command=lambda: toggleInput(breadQuantity, breadLabel, bread, 9), variable=bread).grid(column=0, row=8)
breadLabel = tk.Label(root, text='How Much?:')
breadQuantity = tk.Entry(root)

tk.Checkbutton(root, text="Eggs ($3)", command=lambda: toggleInput(eggsQuantity, eggsLabel, eggs, 12), variable=eggs).grid(column=0, row=11)
eggsLabel = tk.Label(root, text='How Much?:')
eggsQuantity = tk.Entry(root)

tk.Checkbutton(root, text="Fruits ($4)", command=lambda: toggleInput(fruitsQuantity, fruitsLabel, fruits, 15), variable=fruits).grid(column=0, row=14)
fruitsLabel = tk.Label(root, text='How Much?:')
fruitsQuantity = tk.Entry(root)

# Submit
tk.Button(root, text='Submit', command=checkout).grid(column=0, row=17)
root.mainloop()