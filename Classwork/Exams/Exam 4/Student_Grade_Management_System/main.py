from colorama import Style, Fore, Back, init
from os import system, name

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
        Student.students.append(self)


    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    def viewGrades(self):
        for courseName, grade in self.grades.items():
            print(f"{courseName.capitalize()}: {grade}%")

    def addGrade(self, courseName: str, grade: int = 100):
        if courseName in self.grades:
            print("Grade Already Exists In Gradebook. Would you like to overwrite it? (y/n)")
            while True:
                choice = input().lower()
                if choice == "y":
                    break
                elif choice == "n":
                    return
                else:
                    print("Invalid Input. Please enter 'y' or 'n'.")

        if not isinstance(grade, int):
            print("Grade Must Be An Integer.")
            return
        
        if grade < 0 or grade > 100:
            print("Grade Must Be Between 0 and 100.")
            return

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
        if Student.isInt(total / length):
            return int(total / length)
        else:
            return round(total / length, 2)
    
    @staticmethod
    def isInt(num: float):
        return num == int(num)
    
def clearOutput():
    system("cls" if name == "nt" else "clear")

def space(times: int = 1):
    for i in range(times):
        print()

student = None

debug = False

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

clearOutput()

print(Style.BRIGHT + Fore.GREEN + "Welcome To The Student Grade Management System!!!")
print(Style.BRIGHT + Fore.GREEN + "=================================================")

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
        space(2)

    if not debug:
        clearOutput()


    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]

    print(Fore.GREEN + f"Welcome {student.fullName}!")
    space(1)

    print(colors[0] + "1. Add A Grade.")
    print(colors[1] + "2. Remove A Grade.")
    print(colors[2] + "3. Modify A Grade.")
    print(colors[3] + "4. Calculate Average.")
    print(colors[4] + "5. Change Student.")
    print(colors[5] + "6. View Grades.")
    print(colors[6] + "7. View Classmates.")
    print(Back.RED + "Press Ctrl + C To Exit The Program at ANY TIME.")
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
        student.viewGrades()
    elif userChoice == 7:
        print([classmate.fullName for classmate in Student.students])
    elif userChoice == 0:
        break

    input("Press Enter To Continue...")

    if not debug:
        clearOutput()