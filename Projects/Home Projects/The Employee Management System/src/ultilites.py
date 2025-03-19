from typing import Optional
from employee import Employee, Developer, Manager, CEO, Janitor, SecurityGuard, ITSupport
from employee_utillities_shared import listItems, totalEmployeeDict


def read_employee_data(file_path):
    global totalEmployeeDict  # Declare totalEmployeeDict as a global variable
    totalEmployeeDict = {
        "Employee": [],
        "Developer": [],
        "Manager": [],
        "CEO": [],
        "Janitor": [],
        "SecurityGuard": [],
        "ITSupport": []
    }
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(': ')
            emp_type = data[0]
            first, last = data[1].split(' ')
            phone = data[2]
            pay = data[3]
            additional_data = data[4:]

            if emp_type == "Employee":
                totalEmployeeDict["Employee"] = Employee(first, last, phone, pay)
            elif emp_type == "Developer":
                totalEmployeeDict["Developer"] = Developer(first, last, phone, pay, additional_data)
            elif emp_type == "Manager":
                totalEmployeeDict["Manager"] = Manager(first, last, phone, pay, additional_data)
            elif emp_type == "CEO":
                totalEmployeeDict["CEO"] = CEO(first, last, phone, pay, additional_data[:-1], additional_data[-1])
            elif emp_type == "Janitor":
                totalEmployeeDict["Janitor"] = Janitor(first, last, phone, pay, additional_data)
            elif emp_type == "SecurityGuard":
                totalEmployeeDict["SecurityGuard"] = SecurityGuard(first, last, phone, pay, additional_data)
            elif emp_type == "ITSupport":
                totalEmployeeDict["ITSupport"] = ITSupport(first, last, phone, pay)
    
    return totalEmployeeDict