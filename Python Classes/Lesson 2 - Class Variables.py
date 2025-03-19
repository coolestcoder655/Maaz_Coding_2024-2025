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

print(Employee.employeeNumber)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.employeeNumber)