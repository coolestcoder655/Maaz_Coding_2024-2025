# Write a  Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date, datetime


class Person():
    def __init__(self, name: str, COO: str, DOB: date):
        self.name = name
        self.COO = COO
        self.DOB = DOB

    @property
    def age(self):
        today = date.today()
        return ((today.year) - self.DOB.year)
    

newPerson = Person(
    name="Maaz",
    COO="America",
    DOB=datetime(2012, 1, 24)
)

print(newPerson.name)

print(newPerson.COO)

print(newPerson.DOB)

print(newPerson.age)