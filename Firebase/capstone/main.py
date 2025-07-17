from firebase_admin import firestore, initialize_app
from firebase_admin.credentials import Certificate
from classes import Student
import tkinter as tk
from tkinter import ttk
from typing import Optional

# Firebase Init
cred = Certificate(r"examAccount.json")
initialize_app(cred)

db = firestore.client().collection('students')

def addStudent(student: Student):
    # exams = list()
    # for exam in student.exams:
    #     examData = {
    #         "exam_date": str(exam.exam_date),
    #         "subject": exam.subject,
    #         "score": exam.score,
    #         "max_score": exam.max_score,
    #     }
    #     exams.append(examData)

    studentData = {
        'name': student.name,
        'grade': student.grade,
    }
    db.add(studentData)
    studentRef = list(db.where('name', '==', student.name).stream())


    for exam in student.exams:
        exam = {
            'exam_date': str(exam.exam_date),
            'max_score': exam.max_score,
            'score': exam.score,
            'subject': exam.subject,
        }
        for doc in studentRef:
            docRef = db.document(doc.id)
            docRef.collection('exams').add(exam)

    return

studentSelection: Optional[Student] = None


# ========================= UI ================================
root = tk.Tk()
root.title("Student Exam Performance Tracker")
root.geometry("720x500")
root.resizable(False, False)

# --- Top Bar ---
top_frame = tk.Frame(root, padx=10, pady=10)
top_frame.pack(fill="x")

tk.Label(top_frame, text="Select Student:").pack(side="left", padx=(0, 5))
student_menu = ttk.Combobox(top_frame, values=["Alice Johnson"], state="readonly")
student_menu.set("Alice Johnson")
student_menu.pack(side="left")

tk.Button(top_frame, text="Add Student").pack(side="left", padx=5)
tk.Button(top_frame, text="Remove Student").pack(side="left", padx=5)

# --- Exam Records Title and Buttons ---
record_frame = tk.Frame(root, padx=10, pady=10)
record_frame.pack(fill="x")

btn_frame = tk.Frame(record_frame)
btn_frame.pack(fill="x", pady=(0, 10))

tk.Label(record_frame, text="Exam Records", font=("Segoe UI", 10, "bold")).pack(anchor="w")

tk.Button(btn_frame, text="+ Add Exam").pack(side="left")
tk.Button(btn_frame, text="Edit Exam").pack(side="left", padx=5)
tk.Button(btn_frame, text="Delete Exam").pack(side="left", padx=5)
tk.Button(btn_frame, text="View Statistics").pack(side="right")

# --- Table (Static) ---
columns = ("Subject", "Score", "Total", "Percentage", "Date", "Actions")
tree = ttk.Treeview(record_frame, columns=columns, show="headings", height=5)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100 if col != "Actions" else 70)
tree.pack(fill="x")
tree.pack(fill="x")

# Example static data
tree.insert("", "end", values=("Math", "85", "100", "85.0%", "2024-01-15", "✎ 🗑"))
tree.insert("", "end", values=("Science", "92", "100", "92.0%", "2024-01-18", "✎ 🗑"))

# --- Performance Summary ---
summary_frame = tk.Frame(root, padx=10, pady=10)
summary_frame.pack(fill="x", pady=(15, 10))

tk.Label(summary_frame, text="Average Score\n88.5%", relief="solid", padx=10, pady=10).pack(side="left", expand=True, fill="x", padx=5)
tk.Label(summary_frame, text="Highest Score\n92.0%", relief="solid", padx=10, pady=10).pack(side="left", expand=True, fill="x", padx=5)
tk.Label(summary_frame, text="Total Exams\n2", relief="solid", padx=10, pady=10).pack(side="left", expand=True, fill="x", padx=5)

# --- Bottom Info Bar ---
footer = tk.Label(root, text="Student: Alice Johnson       Last Updated: 2024-01-20 09:45 AM", relief="sunken", anchor="w", padx=5, pady=5)
footer.pack(fill="x", side="bottom")

root.mainloop()
