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
from tkinter import messagebox as mb
from json import dump

root = tk.Tk()
root.title('Food Delivery App')
root.geometry('300x425')

def checkout():
    global milk, bread, eggs, nameEntry, addressEntry

    def makeInt(num: float):
        if int(num) == num:
            return int(num)
        else:
            return num
\

    menu = {
        'milk': 2,
        'bread': 1.5,
        'eggs': 3,
        'fruits': 4
    }

    sumOfList = set()

    isMilk = milk.get()
    isEggs = eggs.get()
    isBread = bread.get()
    isFruits = fruits.get()
    name = nameEntry.get()
    address = addressEntry.get()

    if isMilk:
        sumOfList.add(milkQuantity.get() * menu.get('milk', 0))

    if isBread:
        sumOfList.add(breadQuantity.get() * menu.get('bread', 0))

    if isEggs:
        sumOfList.add(eggsQuantity.get() * menu.get('eggs', 0))

    if isFruits:
        sumOfList.add(fruitsQuantity.get() * menu.get('fruits', 0))

    total = sum(sumOfList)
    
    confirm = mb.askyesno(title='Confirm Order', message=f'Would you like to confirm this order?\nTotal: {total}')
    if confirm:
        mb.showinfo(title='Order Place', message='Your order has been placed. Thank you!')
        receipt = {
            'name': name,
            'address': address,
            'total': total,
        }

        with open('receipt.json', w) as file:
            file.write('')
            dump(file, receipt)

# Name + Address
tk.Label(root, text='Name:').pack()
nameEntry = tk.Entry(root).pack()

tk.Label(root, text='Address:').pack()
addressEntry = tk.Entry(root).pack()

# Product Selection
milk = tk.BooleanVar(value=True)
bread = tk.BooleanVar(value=True)
eggs = tk.BooleanVar(value=True)
fruits = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Milk ($2)", variable=milk, ).pack()
if milk.get():
    tk.Label(root, text='How Much?:').pack()
    milkQuantity = tk.Entry(root).pack()

tk.Checkbutton(root, text="Bread ($1.50)", variable=bread, ).pack()
if bread.get():
    tk.Label(root, text='How Much?:').pack()
    breadQuantity = tk.Entry(root).pack()

tk.Checkbutton(root, text="Eggs ($3)", variable=eggs, ).pack()
if eggs.get():
    tk.Label(root, text='How Much?:').pack()
    eggsQuantity = tk.Entry(root).pack()

tk.Checkbutton(root, text="Fruits ($4)", variable=fruits, ).pack()
if fruits.get():
    tk.Label(root, text='How Much?:').pack()
    fruitsQuantity = tk.Entry(root).pack()

# Submit
tk.Button(root, text='Submit', command=checkout, ).pack()


root.mainloop()