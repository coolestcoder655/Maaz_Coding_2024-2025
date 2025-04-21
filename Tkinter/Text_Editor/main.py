import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog, messagebox

currentOpenFile = None

def openFile(mainWindow: tk.Tk, textEdit: tk.Text):
    filePath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("TypeScript Files", "*.ts"), ("Javascript Files", "*.js")])
    global currentOpenFile
    currentOpenFile = filePath

    if filePath == " ":
        messagebox.askokcancel("No File", "No file has been opened.")
        currentOpenFile = None
        return
    
    textEdit.delete(1.0, tk.END)
    with open(filePath, "r") as file:
        content = file.read()

    textEdit.insert(tk.END, content)
    mainWindow.title(f"Opened File: {filePath}")

def saveFile(mainWindow: tk.Tk, textEdit: tk.Text):
    filePath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("TypeScript Files", "*.ts"), ("Javascript Files", "*.js")])

    if not filePath:
        return
    
    with open(filePath, "w") as file:
        content = textEdit.get(1.0, tk.END)
        file.write(content)

    mainWindow.title(f"Opened File: {filePath}")

def createNewFile(mainWindow: tk.Tk, textEdit: tk.Text):
    newfileName = simpledialog.askstring("New File Name?", "Please enter the new file name.")

    try:
        with open(newfileName, "x") as file:
            file.write("")

    except FileExistsError as f:
        messagebox.showerror("ERROR: FILE EXISTS", message=f)

def isFileChanged(textEdit: tk.Text):
    global currentOpenFile
    with open(currentOpenFile, "r") as file:
        original = file.read()

    modified = textEdit.get(1.0, tk.END)

    try:
        for i, (char1, char2) in enumerate(zip(original, modified)):
            if char1 != char2:
                raise Exception

        # Handle extra characters
        if len(original) < len(modified):
            for i in range(len(original), len(modified)):
                raise Exception
        elif len(original) > len(modified):
            for i in range(len(modified), len(original)):
                raise Exception

    except Exception:
        return True
    else:
        return False

def onCloseConfirmation(mainWindow: tk.Tk, textEdit: tk.Text):
    global currentOpenFile
    if not currentOpenFile is None:
        if isFileChanged(textEdit=textEdit):
            if messagebox.askyesno("Confirm Exit.", "Are you sure you want to exit without saving?"):
                currentOpenFile = None
                mainWindow.destroy()
                return
            else:
                return
        else:
            currentOpenFile = None
            mainWindow.destroy()
            return
    else:
        mainWindow.destroy()
        return



def main():
    mainWindow = tk.Tk()
    mainWindow.title("Text Editor")
    mainWindow.rowconfigure(0, minsize=400)
    mainWindow.columnconfigure(1, minsize=250)

    textEdit = tk.Text(mainWindow, font="Helvetica 18")
    textEdit.grid(row=0, column=1)

    frame = tk.Frame(mainWindow, relief=tk.RAISED, bd=2)
    saveButton = tk.Button(frame, text="Save", command=lambda: saveFile(mainWindow=mainWindow, textEdit=textEdit))
    openButton = tk.Button(frame, text="Open", command=lambda: openFile(mainWindow=mainWindow, textEdit=textEdit))
    newFileButton = tk.Button(frame, text="New File", command=lambda: createNewFile(mainWindow=mainWindow, textEdit=textEdit))

    saveButton.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    openButton.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    newFileButton.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    mainWindow.bind("<Control-s>", func=lambda x: saveFile(mainWindow=mainWindow, textEdit=textEdit))
    mainWindow.bind("<Control-o>", func=lambda x: openFile(mainWindow=mainWindow, textEdit=textEdit))
    mainWindow.bind("<Control-n>", func=lambda x: createNewFile(mainWindow=mainWindow, textEdit=textEdit))


    mainWindow.protocol("WM_DELETE_WINDOW", func=lambda: onCloseConfirmation(mainWindow=mainWindow, textEdit=textEdit))

    mainWindow.mainloop()


main()