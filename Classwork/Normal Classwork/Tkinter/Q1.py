# Imagine you’re designing a simple app for students to submit feedback after a class. The form collects the student’s name, subject, rating (1 to 5), and whether they would recommend the class to others.

import tkinter as tk
from tkinter import messagebox
import json


def submitForm():
    name = nameInput.get()
    subject = subjectInput.get()
    score = rating.get()
    recommend = wouldRecommend.get()

    print(f"{name=}")
    print(f"{subject=}")
    print(f"{score=}")
    print(f"{wouldRecommend=}")

    if (name.strip() != "" or subject.strip() != "" or score != -1 or wouldRecommend != None):
        submissionData = {
            "name": name,
            "subject": subject,
            "rating": score,
            "wouldRecommend": recommend,
        }

        with open("submissionData.json", "a") as file:
            json.dump(submissionData, file)

    else:
        messagebox.showerror(title="Submit Error", message="One or more fields is empty. Please check.")

root = tk.Tk()
root.geometry("550x175")
root.title("Feedback App")

# Name Input
nameInput = tk.Entry(root)
nameLabel = tk.Label(root, text="Enter Name:")
nameLabel.grid(row=0, column=1, padx=7.5, pady=7.5)
nameInput.grid(row=0, column=2, padx=7.5, pady=7.5)

# Subject Input
subjectInput = tk.Entry(root)
subjectLabel = tk.Label(root, text="Enter Subject")
subjectLabel.grid(row=1, column=1, padx=7.5, pady=7.5)
subjectInput.grid(row=1, column=2, padx=7.5, pady=7.5)

# Radio Selection
rating = tk.IntVar(value=1)

tk.Label(root, text="Rating:").grid(row=2, column=1, padx=7.5, pady=7.5)
tk.OptionMenu(root, rating, 1, 2, 3, 4, 5).grid(row=2, column=2)

# Would Recommend
wouldRecommend = tk.BooleanVar(value=False)

tk.Label(root, text="Would you recommend this class?").grid(row=3, column=1, padx=7.5, pady=7.5)
tk.Radiobutton(root, text="Yes", value=True, variable=wouldRecommend).grid(row=3, column=2)
tk.Radiobutton(root, text="No", value=False, variable=wouldRecommend).grid(row=3, column=3)

tk.Button(root, text="Submit", command=submitForm).grid(row=4, column=1)

tk.mainloop()