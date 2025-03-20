from colorama import Style, Fore, init

init(autoreset=True)

class Student():
    students = []

    @classmethod
    def findStudent(cls, lastName: str, firstName: str):
        lastName = lastName.lower()
        firstName = firstName.lower()
        for student in cls.students:
            if student.lastName.lower() == lastName and student.firstName.lower() == firstName:
                return student
        raise Exception

    def __init__(self, firstName, lastName, grades: dict = dict()):
        self.firstName = firstName
        self.lastName = lastName
        self.grades = grades
        __class__.students.append(self)


    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    def __str__(self):
        return self.grades

    def addGrade(self, courseName: str, grade: int = 100):
        self.grades[courseName] = grade

    def removeGrade(self, courseName: str):
        if not courseName in self.grades:
            print("Grade Not Located In Gradebook.")
            raise ValueError
        else:
            self.grades.pop(courseName, None)
    
    def updateGrade(self, courseName: str, newGrade: int = 100):
        self.grades[courseName] = newGrade
    
    def calculateAverage(self):
        total = 0
        length = len(self.grades)
        total = sum(self.grades.values())
        return float(total / length)
    
    @staticmethod
    def makeIntIfInt():
        pass
    

print(Style.BRIGHT + Fore.GREEN + "Welcome To The Student Grade Management System!!!")
print(Style.BRIGHT + Fore.GREEN + "=================================================")

student = None

debug = False # ADD

myStudent1 = Student(
    "Maaz", 
    "Khokhar", 
    {
        "english": 50, 
        "spanish": 60
    }
)
myStudent2 = Student(
    "John", 
    "Doe", 
    {
        "math": 75, 
        "science": 85
    }
)
myStudent3 = Student(
    "Jane", 
    "Smith", 
    {
        "history": 90, 
        "art": 95
    }
)
myStudent4 = Student(
    "Alice", 
    "Johnson", 
    {
        "biology": 80, 
        "chemistry": 70
    }
)
myStudent5 = Student(
    "Bob", 
    "Brown", 
    {
        "physics": 65, 
        "geography": 55
    }
)


while True:
    if student == None:
        while True:
            try:
                print(Fore.RED + "Please Enter The Student's Last And First Name, Seperated By A Comma And Space (ex: ', '):")
                lastName, firstName = input().split(", ")
                student = Student.findStudent(lastName, firstName)
                break
            except ValueError:
                print("Incorrect Formatting.")
            except Exception:
                print("Student Not Recognized.")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    print(colors[0] + "1. Add A Grade.")
    print(colors[1] + "2. Remove A Grade.")
    print(colors[2] + "3. Modify A Grade.")
    print(colors[3] + "4. Calculate Average.")
    print(colors[4] + "5. Change Student.")
    userChoice = int(input("Enter Your Choice: "))
    if userChoice == 1:
        courseName = input("Enter The Name Of The Course: ")
        while True:
            try:
                grade = int(input("Enter The Grade Of The Course: "))
                break
            except ValueError:
                print("The input has to be a number from 1 to 5. Try Again.")
        student.addGrade(courseName, grade)
    elif userChoice == 2:
        courseName = input("Enter The Name Of The Course: ")
        student.removeGrade(courseName)
    elif userChoice == 3:
        courseName = input("Enter The Name Of The Course: ")
        while True:
            try:
                grade = int(input("Enter The Grade Of The Course: "))
                break
            except:
                print("The input has to be a number from 1 to 5. Try Again.")
        student.updateGrade(courseName, grade)
    elif userChoice == 4:
        print(student.calculateAverage())
    elif userChoice == 5:
        student = None
    elif userChoice == 6:
        print(student.grades)
    elif userChoice == 7:
        print([classmate.fullName for classmate in Student.students])
    elif userChoice == 0:
        break