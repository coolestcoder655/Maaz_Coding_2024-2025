# Parts:
# Part A – Basic Info
# Add Entry fields for:
# Name ✅
# Age ✅
# Contact Number ✅
# Part B – Symptoms
# Use Checkbuttons to let the patient select:
# Fever ✅
# Cough ✅
# Fatigue ✅
# Headache ✅
# Part C – Gender & Appointment
# Use Radiobuttons to select gender (Male, Female, Other). ✅
# Add a dropdown (OptionMenu) to choose appointment type (General, Follow-up, Emergency). ✅
# Part D – Button Functionality
# Show a pop-up summary using messagebox.showinfo(). ✅
# If age is below 12, display a warning messagebox saying “Child patient – Assign pediatrician”. ✅

import tkinter as tk
from tkinter import messagebox
from json import dump

root = tk.Tk()
root.title("Patient Appointment Submitter")
root.geometry("500x200")

def submitAppointment():

    global isFever, isCough, isFatigue, isHeadache, gender, appointmentType
    print(isFever.get())
    print(isHeadache.get())
    print(isFatigue.get())
    print(gender.get())
    print(isCough.get())

    name = nameEntry.get().strip()
    age = ageEntry.get()
    number = numberEntry.get()
    try:
        isFever = isFever.get()
    except:
        isFever = 0
    try:
        isCough = isCough.get()
    except:
        isCough = 0
    try:
        isFatigue = isFatigue.get()
    except:
        isFatigue = 0
    try:
        isHeadache = isHeadache.get()
    except:
        isHeadache = 0
    gender = gender.get()
    appointmentType = appointmentType.get()


    # Checking
    if name == "" or age == "" or number == "" or gender == "None":
        messagebox.showerror(title="Error Submitting Appointment", message="You have not filled out one of the required fields: Name, Age, Contact Number, or Gender")
        return

    if all([isFever == 0, isCough == 0, isFatigue == 0, isHeadache == 0]):
        messagebox.showerror(title="Error Submitting Appointment", message="The patient does not have any symtopms and cannot be examined.")
        return
    
    try:
        if int(age) < 12:
            messagebox.showinfo(title="Refer Child", message="The child is below 12, please refer to a pediatrician.")
    except:
        messagebox.showerror(title="Error Submitting Appointment", message='Invalid Age; Has To Be Number')
        return

    # Converting Symptoms
    symptoms = list()

    if isFever == 1:
        if len(symptoms) == 0:
            symptoms.append("Fever")
        else:
            symptoms.append(", Fever")

    if isCough == 1:
        if len(symptoms) == 0:
            symptoms.append("Coughing")
        else:
            symptoms.append(", Coughing")

    if isFatigue == 1:
        if len(symptoms) == 0:
            symptoms.append("Fatigue")
        else:
            symptoms.append(", Fatigue")

    if isHeadache == 1:
        if len(symptoms) == 0:
            symptoms.append("Headaches")
        else:
            symptoms.append(", Headaches")

    submissionData = {
        "name": name,
        "age": age,
        "contactNumber": number,
        "gender": gender,
        "appointmentType": appointmentType,
        "symptoms": symptoms
    }

    def printSymptoms():
        symptomString = str()
        for symptom in symptoms:
            symptomString += f'{symptom}, '
        
        return symptomString

    messagebox.showinfo(title='Summary', message=f'Name: {name}\nAge: {age}\nContact Number: {number}\nGender: {gender}\nAppointment Type: {appointmentType}\nSymptoms: {printSymptoms()}')


    with open("appointments.json", "a") as file:
        dump(submissionData, file)


# Name
tk.Label(root, text="Name:").grid(row=0, column=1)
nameEntry = tk.Entry(root)
nameEntry.grid(row=0, column=2)

# Age
tk.Label(root, text="Age:").grid(row=1, column=1)
ageEntry = tk.Entry(root)
ageEntry.grid(row=1, column=2)

# Contact Number
tk.Label(root, text="Contact Number:").grid(row=2, column=1)
numberEntry = tk.Entry(root)
numberEntry.grid(row=2, column=2)

# Symtoms 
tk.Label(root, text="Please select the symptoms").grid(row=3, column=1)


isFever = tk.IntVar(value=0)
isCough = tk.IntVar(value=0)
isFatigue = tk.IntVar(value=0)
isHeadache = tk.IntVar(value=0)

tk.Checkbutton(root, text="Fever", variable=isFever).grid(row=4, column=1)
tk.Checkbutton(root, text="Coughing", variable=isCough).grid(row=4, column=2)
tk.Checkbutton(root, text="Fatigue", variable=isFatigue).grid(row=4, column=3)
tk.Checkbutton(root, text="Headaches", variable=isHeadache).grid(row=4, column=4)


# Gender
tk.Label(root, text="Gender: ").grid(row=5, column=1)

global gender
gender = tk.StringVar(value="None")
tk.Radiobutton(root, variable=gender, text="Male", value="male").grid(row=5, column=2)
tk.Radiobutton(root, variable=gender, text="Female", value="female").grid(row=5, column=3)

# Appointment Type
tk.Label(root, text="Appointment Type: ").grid(row=6, column=1)

global appointmentType
appointmentType = tk.StringVar(value="General")
appointmentTypeSelector = tk.OptionMenu(root, appointmentType, "General", "Follow Up", "Emergency")
appointmentTypeSelector.grid(row=6, column=2)

# Summary Popup + Submit Button
tk.Button(root, text="Submit", command=lambda: submitAppointment()).grid(row=7, column=1)

tk.mainloop()