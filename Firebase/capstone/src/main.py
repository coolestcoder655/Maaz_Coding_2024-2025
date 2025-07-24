import tkinter as tk
from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, messagebox
from tkinter.messagebox import showinfo, showerror
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox, Treeview
from firebase_admin import firestore, initialize_app, auth
from firebase_admin.credentials import Certificate
from firebase_admin.auth import UserRecord, create_user
from classes import Student, Exam
from typing import Optional
from datetime import datetime, date
from requests import post

cred = Certificate("src/examAccount.json")
initialize_app(cred)

apiKey: str = "AIzaSyAHNzGuixFM3e5GORnyvbKoGl-NZMMkMfs"

isLoggedIn: bool = False
user: Optional[dict[str, str | bool]] = None


def createUserViaEmail(email: str, password: str) -> UserRecord | None:
    try:
        user = create_user(email=email, password=password)
        return user
    except Exception as e:
        print(f'|||ERROR|||:\n{e}')
        return None
    

def loginViAEmailPassword(email: str, password: str) -> dict[str, str | bool] | bool:
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={apiKey}"
    data: dict[str, str | bool] = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = post(url, json=data)
    responseData: dict[str, str | bool] = response.json()

    if response.ok:
        return responseData
    
    else:
        print(f'Error with logging in. Please try again.')
        return False

def emailLogin() -> None:
    dialog = tk.Toplevel(loginRoot)
    dialog.title("Email Login")
    dialog.geometry("300x170")
    dialog.resizable(False, False)
    dialog.grab_set()
    dialog.transient(loginRoot)

    # Frame for padding
    frame = tk.Frame(dialog, padx=20, pady=15)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Email:", anchor="w").grid(row=0, column=0, sticky="w", pady=(0, 8))
    email_entry = tk.Entry(frame, width=28)
    email_entry.grid(row=0, column=1, pady=(0, 8))
    email_entry.focus_set()  # Auto-focus on the email field

    tk.Label(frame, text="Password:", anchor="w").grid(row=1, column=0, sticky="w", pady=(0, 8))
    password_entry = tk.Entry(frame, width=28, show="*")
    password_entry.grid(row=1, column=1, pady=(0, 8))
    password_entry.bind("<Return>", lambda event: onLogin())

    def onLogin():
        global isLoggedIn, user
        email = email_entry.get()
        password = password_entry.get()
        result = loginViAEmailPassword(email, password)
        if isinstance(result, dict):
            showinfo("Success", "Logged in successfully!")
            dialog.destroy()
            loginRoot.destroy()  # Close the login window
            isLoggedIn = True
            user = result
        else:
            showerror("Error", "Login failed. Please check your credentials.")

    login_btn = tk.Button(frame, text="Login", width=18, command=onLogin)
    login_btn.grid(row=2, column=0, columnspan=2, pady=(10, 0))

def googleLogin() -> None:
    pass

# 'hello@gmail.com' '123456'

db = firestore.client().collection('students')

# Global variables
studentSelection: Optional[Student] = None
current_student_doc_id: Optional[str] = None

def loadStudentsFromFirebase():
    """Load all students from Firebase"""
    try:
        students = []
        docs = db.stream()
        for doc in docs:
            student_data = doc.to_dict()
            student_name = student_data.get('name', '')
            students.append(student_name)
        return students
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load students: {str(e)}")
        return []

def getStudentExams(student_name: str):
    """Get all exams for a specific student"""
    try:
        student_docs = list(db.where('name', '==', student_name).stream())
        if not student_docs:
            return []
        
        global current_student_doc_id
        current_student_doc_id = student_docs[0].id
        
        exams = []
        exam_docs = db.document(current_student_doc_id).collection('exams').stream()
        for exam_doc in exam_docs:
            exam_data = exam_doc.to_dict()
            exam = Exam(
                subject=exam_data.get('subject', ''),
                score=exam_data.get('score', 0),
                max_score=exam_data.get('max_score', 100),
                exam_date=datetime.strptime(exam_data.get('exam_date', str(date.today())), '%Y-%m-%d').date()
            )
            exams.append((exam, exam_doc.id))
        return exams
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load exams: {str(e)}")
        return []

def addStudentToFirebase(student_name: str):
    """Add a new student to Firebase"""
    try:
        studentData = {
            'name': student_name,
            'grade': 0,
        }
        db.add(studentData)
        messagebox.showinfo("Success", f"Student '{student_name}' added successfully!")
        refreshStudentList()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add student: {str(e)}")

def removeStudentFromFirebase(student_name: str):
    """Remove a student and all their exams from Firebase"""
    try:
        student_docs = list(db.where('name', '==', student_name).stream())
        if student_docs:
            doc_id = student_docs[0].id
            # Delete all exams first
            exam_docs = db.document(doc_id).collection('exams').stream()
            for exam_doc in exam_docs:
                exam_doc.reference.delete()
            # Delete student document
            db.document(doc_id).delete()
            messagebox.showinfo("Success", f"Student '{student_name}' removed successfully!")
            refreshStudentList()
            clearExamTable()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove student: {str(e)}")

def addExamToFirebase(subject: str, score: int, max_score: int, exam_date: str):
    """Add an exam to the current student"""
    try:
        if not current_student_doc_id:
            messagebox.showerror("Error", "No student selected!")
            return
        
        exam_data = {
            'exam_date': exam_date,
            'max_score': max_score,
            'score': score,
            'subject': subject,
        }
        db.document(current_student_doc_id).collection('exams').add(exam_data)
        messagebox.showinfo("Success", "Exam added successfully!")
        updateStudentGrade()
        loadStudentData()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add exam: {str(e)}")

def updateExamInFirebase(exam_id: str, subject: str, score: int, max_score: int, exam_date: str):
    """Update an exam in Firebase"""
    try:
        if not current_student_doc_id:
            messagebox.showerror("Error", "No student selected!")
            return
        
        exam_data = {
            'exam_date': exam_date,
            'max_score': max_score,
            'score': score,
            'subject': subject,
        }
        db.document(current_student_doc_id).collection('exams').document(exam_id).update(exam_data)
        messagebox.showinfo("Success", "Exam updated successfully!")
        updateStudentGrade()
        loadStudentData()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update exam: {str(e)}")

def calculateOverallGrade():
    """Calculate the overall grade for the current student based on all exams"""
    try:
        if not current_student_doc_id:
            return 0.0
        
        exam_docs = db.document(current_student_doc_id).collection('exams').stream()
        total_percentage = 0
        exam_count = 0
        
        for exam_doc in exam_docs:
            exam_data = exam_doc.to_dict()
            score = exam_data.get('score', 0)
            max_score = exam_data.get('max_score', 100)
            
            if max_score > 0:  # Avoid division by zero
                percentage = (score / max_score) * 100
                total_percentage += percentage
                exam_count += 1
        
        return total_percentage / exam_count if exam_count > 0 else 0.0
    except Exception as e:
        print(f"Error calculating grade: {str(e)}")
        return 0.0

def updateStudentGrade():
    """Update the student's overall grade in Firebase"""
    try:
        if not current_student_doc_id:
            return
        
        overall_grade = calculateOverallGrade()
        db.document(current_student_doc_id).update({'grade': overall_grade})
        print(f"Student grade updated to: {overall_grade:.1f}%")
    except Exception as e:
        print(f"Error updating student grade: {str(e)}")

def deleteExamFromFirebase(exam_id: str):
    """Delete an exam from Firebase"""
    try:
        if not current_student_doc_id:
            messagebox.showerror("Error", "No student selected!")
            return
        
        db.document(current_student_doc_id).collection('exams').document(exam_id).delete()
        messagebox.showinfo("Success", "Exam deleted successfully!")
        updateStudentGrade()
        loadStudentData()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete exam: {str(e)}")

# UI Helper Functions
def refreshStudentList():
    """Refresh the student dropdown menu"""
    students = loadStudentsFromFirebase()
    student_menu['values'] = students
    if students:
        student_menu.set(students[0])
        loadStudentData()
    else:
        student_menu.set("")
        clearExamTable()

def clearExamTable():
    """Clear all items from the exam table"""
    for item in tree.get_children():
        tree.delete(item)
    updateSummaryStats([], 0)
    overall_label.config(text="Overall Grade\n0.0%")

def loadStudentData():
    """Load exam data for the selected student"""
    selected_student = student_menu.get()
    if not selected_student:
        clearExamTable()
        return
    
    exams = getStudentExams(selected_student)
    clearExamTable()
    
    total_score = 0
    total_exams = len(exams)
    
    for exam, exam_id in exams:
        percentage = (exam.score / exam.max_score) * 100
        total_score += percentage
        
        tree.insert("", "end", values=(exam.subject, exam.score,exam.max_score,f"{percentage:.1f}%",exam.exam_date.strftime("%Y-%m-%d"),"🗑"), tags=(exam_id,))
    
    average_score = total_score / total_exams if total_exams > 0 else 0
    
    # Ensure the student's grade is up to date
    if total_exams > 0:
        updateStudentGrade()
    
    updateSummaryStats(exams, average_score, 0, total_exams)

def getCurrentStudentGrade():
    """Get the current student's overall grade from Firebase"""
    try:
        if not current_student_doc_id:
            return 0.0
        
        student_doc = db.document(current_student_doc_id).get()
        if student_doc.exists:
            student_data = student_doc.to_dict()
            if student_data:
                return student_data.get('grade', 0.0)
        return 0.0
    except Exception as e:
        print(f"Error getting student grade: {str(e)}")
        return 0.0

def updateSummaryStats(exams, average_score, highest_percentage=0, total_exams=0):
    """Update the summary statistics display"""
    avg_label.config(text=f"Average Score\n{average_score:.1f}%")
    total_label.config(text=f"Total Exams\n{total_exams}")
    
    # Get and display overall grade
    overall_grade = getCurrentStudentGrade()
    overall_label.config(text=f"Overall Grade\n{overall_grade:.1f}%")
    
    # Update footer
    selected_student = student_menu.get()
    current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    footer.config(text=f"Student: {selected_student}       Overall Grade: {overall_grade:.1f}%       Last Updated: {current_time}")

# UI Event Handlers
def onStudentChange():
    """Handle student selection change"""
    loadStudentData()

def onAddStudent():
    """Handle add student button click"""
    student_name = askstring("Add Student", "Enter student name:")
    if student_name and student_name.strip():
        addStudentToFirebase(student_name.strip())

def onRemoveStudent():
    """Handle remove student button click"""
    selected_student = student_menu.get()
    if not selected_student:
        messagebox.showwarning("Warning", "No student selected!")
        return
    
    if messagebox.askyesno("Confirm", f"Are you sure you want to remove '{selected_student}' and all their exams?"):
        removeStudentFromFirebase(selected_student)

def onAddExam():
    """Handle add exam button click"""
    if not student_menu.get():
        messagebox.showwarning("Warning", "Please select a student first!")
        return
    
    # Create dialog for exam input
    dialog = Toplevel(root)
    dialog.title("Add Exam")
    dialog.geometry("300x200")
    dialog.resizable(False, False)
    dialog.grab_set()
    
    # Center the dialog
    dialog.transient(root)
    
    # Form fields
    Label(dialog, text="Subject:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    subject_entry = Entry(dialog, width=20)
    subject_entry.grid(row=0, column=1, padx=10, pady=5)
    
    Label(dialog, text="Score:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    score_entry = Entry(dialog, width=20)
    score_entry.grid(row=1, column=1, padx=10, pady=5)
    
    Label(dialog, text="Max Score:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    max_score_entry = Entry(dialog, width=20)
    max_score_entry.insert(0, "100")
    max_score_entry.grid(row=2, column=1, padx=10, pady=5)
    
    Label(dialog, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    date_entry = Entry(dialog, width=20)
    date_entry.insert(0, date.today().strftime("%Y-%m-%d"))
    date_entry.grid(row=3, column=1, padx=10, pady=5)
    
    def submit_exam():
        try:
            subject = subject_entry.get().strip()
            score = int(score_entry.get())
            max_score = int(max_score_entry.get())
            exam_date = date_entry.get().strip()
            
            if not subject:
                messagebox.showerror("Error", "Subject cannot be empty!")
                return
            
            # Validate date format
            datetime.strptime(exam_date, "%Y-%m-%d")
            
            if score < 0 or score > max_score:
                messagebox.showerror("Error", "Score must be between 0 and max score!")
                return
            
            addExamToFirebase(subject, score, max_score, exam_date)
            dialog.destroy()
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid numbers for score and max score!")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid date format! Use YYYY-MM-DD")
    
    Button(dialog, text="Add Exam", command=submit_exam).grid(row=4, column=0, columnspan=2, pady=20)

def onEditExam():
    """Handle edit exam button click"""
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select an exam to edit!")
        return
    
    # Get the exam data from the selected row
    item = selected[0]
    exam_values = tree.item(item, 'values')
    exam_id = tree.item(item, 'tags')[0] if tree.item(item, 'tags') else None
    
    if not exam_id:
        messagebox.showerror("Error", "Could not find exam ID!")
        return
    
    # Create dialog for exam editing
    dialog = Toplevel(root)
    dialog.title("Edit Exam")
    dialog.geometry("300x200")
    dialog.resizable(False, False)
    dialog.grab_set()
    
    # Center the dialog
    dialog.transient(root)
    
    # Form fields with current values
    Label(dialog, text="Subject:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    subject_entry = Entry(dialog, width=20)
    subject_entry.insert(0, exam_values[0])  # Current subject
    subject_entry.grid(row=0, column=1, padx=10, pady=5)
    
    Label(dialog, text="Score:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    score_entry = Entry(dialog, width=20)
    score_entry.insert(0, str(exam_values[1]))  # Current score
    score_entry.grid(row=1, column=1, padx=10, pady=5)
    
    Label(dialog, text="Max Score:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    max_score_entry = Entry(dialog, width=20)
    max_score_entry.insert(0, str(exam_values[2]))  # Current max score
    max_score_entry.grid(row=2, column=1, padx=10, pady=5)
    
    Label(dialog, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    date_entry = Entry(dialog, width=20)
    date_entry.insert(0, exam_values[4])  # Current date
    date_entry.grid(row=3, column=1, padx=10, pady=5)
    
    def update_exam():
        try:
            subject = subject_entry.get().strip()
            score = int(score_entry.get())
            max_score = int(max_score_entry.get())
            exam_date = date_entry.get().strip()
            
            if not subject:
                messagebox.showerror("Error", "Subject cannot be empty!")
                return
            
            # Validate date format
            datetime.strptime(exam_date, "%Y-%m-%d")
            
            if score < 0 or score > max_score:
                messagebox.showerror("Error", "Score must be between 0 and max score!")
                return
            
            updateExamInFirebase(exam_id, subject, score, max_score, exam_date)
            dialog.destroy()
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid numbers for score and max score!")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid date format! Use YYYY-MM-DD")
    
    Button(dialog, text="Update Exam", command=update_exam).grid(row=4, column=0, columnspan=2, pady=20)

def onTreeClick(event):
    """Handle clicks on the treeview table"""
    item = tree.selection()[0] if tree.selection() else None
    if not item:
        return
    
    # Get the column that was clicked
    column = tree.identify_column(event.x)
    
    # Check if the Actions column (column #6) was clicked
    if column == '#6':  # Actions column
        exam_values = tree.item(item, 'values')
        exam_id = tree.item(item, 'tags')[0] if tree.item(item, 'tags') else None
        
        if not exam_id:
            messagebox.showerror("Error", "Could not find exam ID!")
            return
        
        # Confirm deletion
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete the {exam_values[0]} exam?"):
            deleteExamFromFirebase(exam_id)

def onDeleteExam():
    """Handle delete exam button click"""
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select an exam to delete!")
        return
    
    # Get the exam ID from tags
    item = selected[0]
    exam_values = tree.item(item, 'values')
    exam_id = tree.item(item, 'tags')[0] if tree.item(item, 'tags') else None
    
    if not exam_id:
        messagebox.showerror("Error", "Could not find exam ID!")
        return
    
    if messagebox.askyesno("Confirm", f"Are you sure you want to delete the {exam_values[0]} exam?"):
        deleteExamFromFirebase(exam_id)
    """Handle delete exam button click"""
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select an exam to delete!")
        return
    
    # Get the exam ID from tags
    item = selected[0]
    exam_values = tree.item(item, 'values')
    exam_id = tree.item(item, 'tags')[0] if tree.item(item, 'tags') else None
    
    if not exam_id:
        messagebox.showerror("Error", "Could not find exam ID!")
        return
    
    if messagebox.askyesno("Confirm", f"Are you sure you want to delete the {exam_values[0]} exam?"):
        deleteExamFromFirebase(exam_id)

def onViewStats():
    """Handle view statistics button click"""
    selected_student = student_menu.get()
    if not selected_student:
        messagebox.showwarning("Warning", "Please select a student first!")
        return
    
    exams = getStudentExams(selected_student)
    if not exams:
        messagebox.showinfo("Statistics", "No exams found for this student!")
        return
    
    # Calculate detailed statistics
    scores = [exam.score for exam, _ in exams]
    max_scores = [exam.max_score for exam, _ in exams]
    percentages = [(exam.score / exam.max_score) * 100 for exam, _ in exams]
    subjects = [exam.subject for exam, _ in exams]
    
    avg_percentage = sum(percentages) / len(percentages)
    min_percentage = min(percentages)
    max_percentage = max(percentages)
    
    # Find best and worst subjects
    subject_avg = {}
    subject_count = {}
    for exam, _ in exams:
        subject = exam.subject
        percentage = (exam.score / exam.max_score) * 100
        if subject in subject_avg:
            subject_avg[subject] += percentage
            subject_count[subject] += 1
        else:
            subject_avg[subject] = percentage
            subject_count[subject] = 1
    
    for subject in subject_avg:
        subject_avg[subject] /= subject_count[subject]
    
    best_subject = max(subject_avg, key=lambda x: subject_avg[x]) if subject_avg else "N/A"
    worst_subject = min(subject_avg, key=lambda x: subject_avg[x]) if subject_avg else "N/A"
    
    # Get overall grade
    overall_grade = getCurrentStudentGrade()
    
    stats_text = f"""
Statistics for {selected_student}:

Total Exams: {len(exams)}
Average Score: {avg_percentage:.1f}%
Lowest Score: {min_percentage:.1f}%
Overall Grade: {overall_grade:.1f}%

Best Subject: {best_subject} ({subject_avg.get(best_subject, 0):.1f}%)
Worst Subject: {worst_subject} ({subject_avg.get(worst_subject, 0):.1f}%)
"""
    
    messagebox.showinfo("Detailed Statistics", stats_text)


# ========================= UI ================================
loginRoot: tk.Tk = tk.Tk()
loginRoot.title('Login Menu')
loginRoot.geometry('400x250')
loginRoot.resizable(False, False)

main_frame = tk.Frame(loginRoot, padx=30, pady=30)
main_frame.pack(expand=True, fill="both")

tk.Label(main_frame, text="Welcome! Please choose a login method:", font=("Arial", 13, "bold")).pack(pady=(0, 25))

btn_frame = tk.Frame(main_frame)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text='Login With Email + Password', width=25, command=emailLogin).pack(side='top', pady=8)
tk.Button(btn_frame, text='Login With Google', width=25, command=googleLogin).pack(side='top', pady=8)

loginRoot.mainloop()

if not isLoggedIn:
    messagebox.showerror("Error", "You must be logged in to access the main application.")
    exit()

root = Tk()
root.title("Student Exam Performance Tracker")
root.geometry("720x500")
root.resizable(False, False)

# --- Top Bar ---
top_frame = Frame(root, padx=10, pady=10)
top_frame.pack(fill="x")

Label(top_frame, text="Select Student:").pack(side="left", padx=(0, 5))
student_menu = Combobox(top_frame, values=[], state="readonly")
student_menu.pack(side="left")
student_menu.bind("<<ComboboxSelected>>", onStudentChange) # type: ignore

Button(top_frame, text="Add Student", command=onAddStudent).pack(side="left", padx=5)
Button(top_frame, text="Remove Student", command=onRemoveStudent).pack(side="left", padx=5)

# --- Exam Records Title and Buttons ---
record_frame = Frame(root, padx=10, pady=10)
record_frame.pack(fill="x")

btn_frame = Frame(record_frame)
btn_frame.pack(fill="x", pady=(0, 10))

Label(record_frame, text="Exam Records", font=("Segoe UI", 10, "bold")).pack(anchor="w")

Button(btn_frame, text="+ Add Exam", command=onAddExam).pack(side="left")
Button(btn_frame, text="Edit Exam", command=onEditExam).pack(side="left", padx=5)
Button(btn_frame, text="Delete Exam", command=onDeleteExam).pack(side="left", padx=5)
Button(btn_frame, text="View Statistics", command=onViewStats).pack(side="right")

# --- Table ---
columns = ("Subject", "Score", "Total", "Percentage", "Date", "Actions")
tree = Treeview(record_frame, columns=columns, show="headings", height=5)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100 if col != "Actions" else 50)
tree.pack(fill="x")

# Bind click event to handle trash icon clicks
tree.bind("<Button-1>", onTreeClick)

# --- Performance Summary ---
summary_frame = Frame(root, padx=10, pady=10)
summary_frame.pack(fill="x", pady=(15, 10))

avg_label = Label(summary_frame, text="Average Score\n0.0%", padx=10, pady=10)
avg_label.pack(side="left", expand=True, fill="x", padx=5)

total_label = Label(summary_frame, text="Total Exams\n0", padx=10, pady=10)
total_label.pack(side="left", expand=True, fill="x", padx=5)

overall_label = Label(summary_frame, text="Overall Grade\n0.0%", padx=10, pady=10)
overall_label.pack(side="left", expand=True, fill="x", padx=5)

# --- Bottom Info Bar ---
footer = Label(root, text="Student: None       Last Updated: Never", relief="sunken", anchor="w", padx=5, pady=5)
footer.pack(fill="x", side="bottom")

# Initialize the application
refreshStudentList()

root.mainloop()