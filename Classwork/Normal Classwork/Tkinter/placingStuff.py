import tkinter as tk

# Create a Tkinter app that asks the user for their Name, Age, and Favorite Color. ✅
# Use .grid() to lay out the labels and entry fields for Name and Age. ✅
# Use .place() to place the Favorite Color label and input at custom coordinates.✅
# Use .pack() to place a Submit button at the bottom.
# When the user clicks Submit, display a message like: ✅
# “Hello Alice! You are 14 years old and your favorite color is Blue.” ✅
# This message should be shown in a Label at the bottom using .pack(). ✅

def submit():
    result = f"Hello {nameInput.get()}! You are {ageInput.get()} years old and your favorite color is {favColorInput.get()}."
    resultLabel.config(text=result)
    return

root = tk.Tk()
root.title("Data Miner")
root.geometry("500x500")
nameLabel = tk.Label(root, text="Enter Name:")
nameInput = tk.Entry(root)
nameLabel.grid(row=0, column=1, padx=20, pady=20)
nameInput.grid(row=0, column=2)

ageLabel = tk.Label(root, text="Enter Age:")
ageInput = tk.Entry(root)
ageLabel.grid(row=2, column=1, padx=20, pady=20)
ageInput.grid(row=2, column=2)

favColorLabel = tk.Label(root, text="Enter Fav Color:")
favColorInput = tk.Entry(root)
favColorLabel.grid(row=3, column=1, padx=20, pady=20)
favColorInput.grid(row=3, column=2)

submitButton = tk.Button(root, text="Submit", command=submit)
submitButton.grid(row=4, column=1)

resultLabel = tk.Label(root, text="")
resultLabel.grid(row=5, column=1)

root.mainloop()