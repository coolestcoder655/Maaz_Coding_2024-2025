import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Buttons")
root.geometry("300x200")

def onChange(var):
    print(var.get())

checkButton = tk.IntVar()
check = tk.Checkbutton(root, text="Check Button", variable=checkButton, command=lambda: onChange(checkButton))
check.pack()

tk.Label(root, text="Choose a Game").pack()

chosen = tk.StringVar(value="None")
tk.Radiobutton(root, text="Monopoly", variable=chosen, value="Monopoly").pack()

tk.Radiobutton(root, text="Uno", variable=chosen, value="Uno").pack()

tk.Radiobutton(root, text="Battleship", variable=chosen, value="Battleship").pack()

def showResult():
    messagebox.showinfo(title="Results", message=chosen.get())

tk.Button(root, text="Submit", command=showResult).pack()


root.mainloop()