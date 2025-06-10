import tkinter as tk

root = tk.Tk()

root.title("My First Window")

root.geometry("300x200")

def buttonFunction():
    label.config(text=textInput.get())
    return

label = tk.Label(root, text="My First Label")
label.pack()
button = tk.Button(root, text="Click me", command=buttonFunction)
textInput = tk.Entry(root)
textInput.pack()
button.pack()
root.mainloop()