import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openFile(window: tk.Tk, textEdit: tk.Text):
    filePath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("TypeScript Files", "*.ts"), ("Javascript Files", "*.js")])

    if not filePath:
        return
    
    textEdit.delete(1.0, tk.END)
    with open(filePath, "r") as file:
        content = file.read()

    textEdit.insert(tk.END, content)
    window.title(f"Opened File: {filePath}")

def saveFile(window: tk.Tk, textEdit: tk.Text):
    filePath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("TypeScript Files", "*.ts"), ("Javascript Files", "*.js")])

    if not filePath:
        return
    
    with open(filePath, "w") as file:
        content = textEdit.get(1.0, tk.END)
        file.write(content)

    window.title(f"Opened File: {filePath}")


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=250)

    textEdit = tk.Text(window, font="Helvetica 18")
    textEdit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    saveButton = tk.Button(frame, text="Save", command=lambda: openFile(window=window, textEdit=textEdit))
    openButton = tk.Button(frame, text="Open", command=lambda: openFile(window=window, textEdit=textEdit))

    saveButton.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    openButton.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", func=lambda x: saveFile(window=window, textEdit=textEdit))
    window.bind("<Control-o>", func=lambda x: openFile(window=window, textEdit=textEdit))


    window.mainloop()


main()