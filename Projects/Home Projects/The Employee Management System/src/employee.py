from typing import Optional
from time import sleep
from random import randint
from enum import Enum
from floormart import Floormart
from employee_utillities_shared import listItems, totalEmployeeDict

class Employee:
    company = "Floormart"
    employeeList = []

    @classmethod
    def fromString(cls, employeeString, newEmpName, jobTitle):
        first, last, phone, pay = employeeString.split("-")   # John-Doe-555-555-5555-100000
        exec(f"{newEmpName} = {jobTitle}(first, last, phone, pay)")
        return newEmpName

    def __init__(self, first, last, phone, pay):    # Employee("John", "Doe", "555-555-5555", 100000)
        self.first = first
        self.last = last
        self.phone = phone
        self.pay = pay
        self.toDoList = []
        self.jobClearance = 1

    @property
    def fullName(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@{self.company.lower()}.employee.net"

    @property
    def expandPhone(self):
        areaCode, actualNumberPt1, actualNumberPt2 = self.phone.split("-")  # 555-555-5555
        actualNumber = f"{actualNumberPt1}-{actualNumberPt2}" # 555-5555
        return (areaCode, actualNumber)     # Returns a Tuple, Area Code: Index 1; Actual Number: Index 2

    def addItem(self, item):
        self.toDoList.append(item)
        return f"The item has been added to {jobTitle} {self.fullName}'s To-Do List."

    def checkOffToDo(self, toDoList):
        listItems(toDoList)
        userChoice = int(input(f"Which Item Would You Like to Remove?: 1 - {len(toDoList)} \n Enter Here: "))
        toDoList.pop(userChoice - 1)
        return "Completed."

class Developer(Employee):
    def __init__ (self, first, last, phone, pay, language: list):
        super().__init__(first, last, phone, pay)
        self.language = language
        self.jobClearance = 5

    def adjustLanguages(self, language, newLanguage: Optional, addMore: bool = False, *args):
        if addMore == False and args:
            return "An inconsistency has been detected. The addMore boolean you have chosen (False) is incompatible with the subsequent introduction of additional arguments."
        elif addMore == True and not args:
            return "An inconsistency has been detected. It appears that you have decided to add more arguments, then did not add any more arguemnts."
        
        choice = None

        while choice != True or False:
            choice = input("Change Languages (Y/N)").lower()

            if choice == "y":
                choice = True
            elif choice == "n":
                choice = False

        if choice == True and newLanguage is None:
            return "An inconsistency has been detected. You have asked for a new language, but you have not provided one."
        
        if choice == True:
            language[0] = newLanguage # [Python, Java, C++]
        
        if addMore == True:
            moreLanguges = list(args)
            language = language + moreLanguges
        return "Completed."

class Manager(Employee):
    def __init__ (self, first, last, phone, pay, manages: list):
        super().__init__(first, last, phone, pay)
        self.manages = manages
        self.jobClearance = 8

    def addEmployees(self, employees, manages):
        print("Adding...")
        manages.append(employees)
        return "Completed."

    def removeEmployees(self, manages):
        listItems(manages)
        userChoice = int(input(f"Which Item Would You Like to Remove?: 1 - {len(manages)} \n Enter Here: "))
        manages.pop(userChoice - 1)
        return "Completed."

class CEO(Employee):
    def __init__ (self, first, last, phone, pay, managesCEO: list, company):
        super().__init__(first, last, phone, pay)
        self.company = company
        self.jobClearance = 10
        self.managesCEO = managesCEO

    def changeCompany(self, company, newCompany):
        company = company.replace(company, newCompany)
        return "Completed."

class Janitor(Employee):
    def __init__ (self, first, last, phone, pay, cleans: list):
        super().__init__(first, last, phone, pay)
        self.cleans = cleans
        self.jobClearance = 3

    def addCleaning(self, cleans, item):
        cleans.append(item)
        return "Completed."

    def completedCleaning(self, cleans):
        listItems(cleans)
        userChoice = int(input(f"Which Item Would You Like to Remove?: 1 - {len(cleans)} \n Enter Here: "))
        cleans.pop(userChoice - 1)
        return "Completed."

class SecurityGuard(Employee):
    def __init__ (self, first, last, phone, pay, secures: list):
        super().__init__(first, last, phone, pay)
        self.secures = secures
        self.jobClearance = 6

    def addSecurityArea(self, secures, item):
        secures.append(item)
        return "Completed."

    def removeSecurityArea(self, secures):
        listItems(secures)
        userChoice = int(input(f"Which Item Would You Like to Remove?: 1 - {len(secures)} \n Enter Here: "))
        secures.pop(userChoice - 1)
        return "Completed."

class ITSupport(Employee):
    def __init__ (self, first, last, phone, pay):
        super().__init__(first, last, phone, pay)
        self.jobClearance = 4