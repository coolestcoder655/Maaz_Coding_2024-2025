import datetime

class Employee:

    raise_amount = 1.04
    employeeNumber = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.employeeNumber += 1

    def fullName(self):
        print(f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employeeString):
        first, last, pay = employeeString.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)


newEmployeeString_1 = "John-Doe-70000"
newEmployeeString_2 = "Steve-Smith-30000"
newEmployeeString_3 = "Jane-Doe-90000"

emp_3 = Employee.from_string(newEmployeeString_1)

date = datetime.date(2016, 7, 11)

print(Employee.is_workday(date))