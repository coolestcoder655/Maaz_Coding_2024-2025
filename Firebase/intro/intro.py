from firebase_admin import firestore, credentials, initialize_app

cred = credentials.Certificate("serviceAccount.json")
initialize_app(cred)

db = firestore.client()
studentRef = db.collection('students')

students = studentRef.stream()

def showStudents():
    for student in students:
        student = student.to_dict()
        name: str = student.get('name', 'N/A')
        subjects: list[str] = student.get('subjects', 'N/A')
        grade: int = int(student.get('grade', 'N/A'))
        print('---------------------------')
        print(f'Name: {name}')
        print(f'Grade: {grade}')
        print(f'Subjects: ', end=' ')
        for subject in subjects:
            subject = subject.capitalize()
            if subject == subjects[-1].capitalize():
                print(subject, end='\n')
            else:
                print(f'{subject},', end=' ')

query = studentRef.where('name', '==', 'Kim').stream()

for doc in query:
    docRef = studentRef.document(doc.id)
    docRef.delete()

gradeQuery = studentRef.where('grade', '>', 5).stream()

for doc in gradeQuery:
    data = doc.to_dict()
    print(data.get('name', 'N/A'))