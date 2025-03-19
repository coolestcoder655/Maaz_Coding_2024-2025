class Student():
    
    def __init__(self, name, marks: list = []):
        self.name = name
        self.marks = marks

    def average(self):
        average = 0
        for mark in self.marks:
            average += mark
        average = average / len(self.marks)
        print(f"Average: {int(average)}")

    @staticmethod
    def schoolName():
        print("Garden Ridge")

student = Student("john", [90, 95, 100])

student.schoolName()