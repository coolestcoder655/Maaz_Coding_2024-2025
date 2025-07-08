from firebase_admin import firestore, initialize_app
from firebase_admin.credentials import Certificate
from classes import Student
import tkinter as tk

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

def selectStudent() -> None:
    print('Selecting Student...')
    return

studentSelected: bool = False


# ========================= UI ================================
root: tk.Tk = tk.Tk()
root.title('Capstone')
root.geometry('500x500')


# ===== Title =====
titleText = 'Student Exam Preformance Tracker'
tk.Label(root,
        text=titleText,
        anchor=tk.CENTER,       
        bg="lightblue",      
        height=3,              
        width=30,              
        bd=3,                  
        font=("Arial", 12, "bold"),    
        fg="red",                
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,           
        wraplength=250,
        ).grid(column=0, row=0, columnspan=3, padx=15, pady=15, )
root.grid_columnconfigure(0, weight=1, )
root.grid_columnconfigure(1, weight=1, )
root.grid_columnconfigure(2, weight=1, )

# ===== Select Student Button =====
tk.Button(root, command=selectStudent, text='View Student', cursor="hand2", ).grid(column=0, row=1, )

root.mainloop()