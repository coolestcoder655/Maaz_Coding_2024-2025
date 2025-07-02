from firebase_admin import firestore, initialize_app
from firebase_admin.credentials import Certificate
from classes import Student, Exam
from datetime import date

# Firebase Init
cred = Certificate(r"capstone\examAccount.json")
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
    studentRef = db.where('name', '==', student.name).stream()


    for exam in student.exams:
        exam = {
            'exam_date': str(exam.exam_date),
            'max_score': exam.max_score,
            'score': exam.score,
            'subject': exam.subject,
        }
        print(exam)
        for doc in studentRef:
            docRef = db.document(doc.id)
            docRef.collection('exams').add(exam)
    
        continue

exams = [
    Exam(subject="Math", score=95, exam_date=date(2024, 6, 1)),
    Exam(subject="Science", score=88, exam_date=date(2024, 6, 5)),
    Exam(subject="English", score=92, exam_date=date(2024, 6, 10))
]

test = Student('Jason', exams)

addStudent(test)