# Objective:
# Build a Tkinter GUI that:
# Collects user input for monthly expenses in different categories.
# Calculates total expenses.
# Plots the result as a pie chart using Matplotlib.
# Embeds the chart directly in the Tkinter window.
# Features Required:
# Tkinter GUI with Label + Entry fields for:
# Food ✅
# Transport ✅
# Utilities ✅
# Entertainment ✅
# A Button to trigger the calculation and display ✅
# Use Matplotlib to create a pie chart showing how money is distributed across the categories
# Use FigureCanvasTkAgg to embed the chart in the Tkinter window

import tkinter as tk
from tkinter import messagebox as mb
import matplotlib.pyplot as plt
from typing import List

def generateColors(listOfX: List[int]) -> List[str]:
    templateColors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    colors: List[str] = []
    index = 0
    for _ in range(1, len(listOfX) + 1):
        index += 1
        if index > (len(templateColors) - 1):
            index = 0
        
        colors.append(templateColors[index])

    return colors

def submit():
    # Grabbing Data From Entries
    food: str = foodEntry.get().strip()
    transport: str = transportEntry.get().strip()
    utilites: str = utiltiesEntry.get().strip()
    entertainment: str = entertainmentEntry.get().strip()

    # Adding Them To List For Easy Manipulation
    listOfItems = [food, transport, utilites, entertainment]
    labels = ['Food', 'Transport', 'Utilties', 'Entertainment']

    # This function clears all entry fields
    def clearFields():
        foodEntry.delete(0, tk.END)
        transportEntry.delete(0, tk.END)
        utiltiesEntry.delete(0, tk.END)
        entertainmentEntry.delete(0, tk.END)

    # Checks if any fields are empty
    if any([x == '' for x in listOfItems]):
        mb.showerror(title='Error Submitting Data', message='One or more fields may be empty. This includes: Food, Transport, Utilites, Entertainment.') # type: ignore
        clearFields()
        return


    # Checks to see if all items in list are convertable
    try:
        listOfItems = [int(x) for x in listOfItems]
        total = sum(listOfItems)
    except:
        mb.showerror(title='Error Submitting Data', message='One or more fields may contain a letter. This includes: Food, Transport, Utilites, Entertainment.') # type: ignore
        clearFields()
        return
    
    # Generates pie chart from values
    plt.pie(listOfItems, labels=labels, normalize=True, autopct="%1.1f%%", shadow=True, colors=generateColors(listOfItems), startangle=90) # type: ignore

    # Generates a center circle and embeds it into the circle
    cc = plt.Circle((0, 0), radius=0.7, fc="white") # type: ignore
    plt.gca().add_artist(cc) # type: ignore
    
    # Equalizes the Axis, Adds A Title, and Shows the Graph To The User
    plt.axis("equal") # type: ignore
    message: str = r"$\it{Expenses}$ $\it{Graph}$ - $\bf{US}$ $\bf{Dollars}$"
    plt.suptitle(message, fontsize=16) # type: ignore
    plt.title(f'Total = ${total:.2f}', fontsize=12) # type: ignore
    plt.show() # type: ignore
    


# Creates a Root Window
root: tk.Tk = tk.Tk()
root.title('Expenses Graph')
root.geometry('450x250')

# Title
# title = tk.Label(root, text='Expenses Graph', font=('Arial', 30, 'bold'), anchor=tk.CENTER, relief=tk.RAISED, wraplength=250)
# title.place(x=100, y=10)

# Food Entry Field
tk.Label(root, text='Food: ',).grid(padx=10, pady=10, column=1, row=1)
foodEntry: tk.Entry = tk.Entry(root)
foodEntry.grid(column=2, row=1)

# Transport Entry Field
tk.Label(root, text='Transportation: ',).grid(padx=10, pady=10, column=1, row=2)
transportEntry: tk.Entry = tk.Entry(root)
transportEntry.grid(column=2, row=2)

# Utilites Entry Field
tk.Label(root, text='Utilties: ',).grid(padx=10, pady=10, column=1, row=3)
utiltiesEntry: tk.Entry = tk.Entry(root)
utiltiesEntry.grid(column=2, row=3)

# Entertainment Entry Field
tk.Label(root, text='Entertainment: ',).grid(padx=10, pady=10, column=1, row=4)
entertainmentEntry: tk.Entry = tk.Entry(root)
entertainmentEntry.grid(column=2, row=4)

# Submit Button
tk.Button(root, text='Caluculate Expenses', command=submit).grid(padx=10, pady=10, column=1, row=5)

root.mainloop()