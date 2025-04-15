import datetime

class Employee:

    raise_amount = 1.04
    employeeNumber = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.employeeNumber += 1

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        self.first = None
        self.last = None

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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.fullName(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullName())


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

dev_1.first = "Jim"
dev_1.fullName = "Corey Schafer"

print(dev_1.first)
print(dev_1.email)
print(dev_1.fullName)

del dev_1.fullName