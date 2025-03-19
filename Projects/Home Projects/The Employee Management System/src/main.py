from typing import Optional
from time import sleep
from random import randint
from enum import Enum
from sys import path
path.append("The%20Employee%20Management%20System/src")
from employee import Employee, Developer, Manager, CEO, Janitor, SecurityGuard, ITSupport
from floormart import Floormart
from state import State
from ultilites import read_employee_data
from employee_utillities_shared import listItems, totalEmployeeDict

# ----------------------------------------------------------------------------------------------------


# Functions:


def securityGuardLockdownToggle(currentState):
    if not lockdown:
        currentState = State.Lockdown
    if lockdown:
        currentState = State.Login

def checkPasscode(correctPasscode):
    override = "CEOOVERRIDE"
    passToCheck = str(input("Please Enter The Passcode To Accsess: "))

    if passToCheck == correctPasscode or passToCheck == override:
        return True
    else:
        return False
def createEmployee(key):
    try:
        if key in totalEmployeeDict:
            for i in totalEmployeeDict[totalEmployeeDict.get(key, ValueError)]:
                x += 1
                if key == "Employee":
                    exec(f"{key}{x} = {key}(i.first, i.last, i.phone, i.pay)")
                elif key == "Developer":
                    exec(f"{key}{x} = {key}(i.first, i.last, i.phone, i.pay, i.language)")
                elif key == "Manager":
                    exec(f"{key}{x} = {key}(i.first, i.last, i.phone, i.pay, i.jobClearance)")

        else: print("No Employees Found.")
    except Exception as e:
        print(f"An Error Occured: {e}")

# ----------------------------------------------------------------------------------------------------

# Variables:

jobTitles = [
    Employee,
    Manager,
    CEO,
    Janitor,
    SecurityGuard,
    ITSupport
    ]



# Initial Setup:
def setup():
    currentState = State.Login



def main():
    currentState = State.Login
    setup()
    employees = read_employee_data('employees.txt')
    x = 0
    

    for x in jobTitles:
        createEmployee(x)

    print("Welcome to Floormart Employee Management System (EMS).")
    while True:
        if currentState == State.Lockdown:                              # Lockdown State
            print("The System is Currently in Lockdown. Please Wait.")
            lockDownChoice = int(input(""))
            if lockDownChoice == "Disable_Lockdown":
                print("Lockdown has been disabled.")
                currentState = State.Login
        elif currentState == State.Login:                               # Login State
            loginChoice = int(input("Please Choose Who You Would Like to Login: \n 1 - Employee \n 2 - Manager \n 3 - CEO \n 4 - Janitor \n 5 - Security Guard \n 6 - IT Support \n 0 - Exit \n Enter Here: "))
            if loginChoice == 1:                                        # Employee Login
                currentState = State.EmployeeMenu
            elif loginChoice == 2:                                      # Manager Login
                managerPasswordInput = checkPasscode("M@n@g3rAccs3ss")
                if managerPasswordInput == True:
                    currentState = State.ManagerMenu
                else:
                    print("Incorrect Password.")
            elif loginChoice == 3:                                      # CEO Login
                CEOPasswordInput = checkPasscode("The_High_Command")
                if CEOPasswordInput == True:
                    CEOPinInput = input("Please Enter The CEO Pin: ")
                    if CEOPinInput == CEOPin:
                        currentState = State.CEOMenu
                    else:
                        print("Incorrect Pin.")
                else:
                    print("Incorrect Password.")

            elif loginChoice == 4:                                      # Janitor Login
                currentState = State.JanitorMenu
            elif loginChoice == 5:                                      # Security Guard Login
                SecurityGuardPasswordInput = checkPasscode("EagleEyes")
                if SecurityGuardPasswordInput == True:
                    currentState = State.SecurityGuardMenu
                else:
                    print("Incorrect Password.")
            elif loginChoice == 6:                                      # IT Support Login
                ITSupportPasswordInput = checkPasscode("N0T_A_SCAMMER")
                if ITSupportPasswordInput == True:
                    currentState = State.ITSupportMenu
                else:
                    print("Incorrect Password.")
            elif loginChoice == 0:                                      # Exit
                currentState = State.Exit
        elif currentState == State.EmployeeMenu:                        # Employee Menu
            employeeChoice = int(input("Please Choose What You Would Like to Do: \n 1 - View To-Do List \n 2 - Add Item To To-Do List \n 3 - Remove Item From To-Do List \n 0 - Exit \n Enter Here: "))
            if employeeChoice == 1:
                print("To-Do List:")
                listItems(toDoList)
            elif employeeChoice == 2:
                item = input("Please Enter The Item You Would Like to Add: ")
                addItem(item)
                print("Item Added.")
            elif employeeChoice == 3:
                checkOffToDo(toDoList)
                print("Item Removed.")
            elif employeeChoice == 0:
                currentState = State.Login
        elif currentState == State.ManagerMenu:                         # Manager Menu
            managerChoice = int(input("Please Choose What You Would Like to Do: \n 1 - View Employees \n 2 - Add Employee \n 3 - Remove Employee \n 4 - Create New Employee \n 0 - Exit \n Enter Here: "))
            if managerChoice == 1:
                print("Employees:")
                listItems(jobTitles)
            elif managerChoice == 2:
                managerAdd = str(input("Please Enter The New Employee Name (Full Name): "))
                print(addEmployee(managerChoice))
            elif managerChoice == 3:
                print(removeEmployee(employee))
            elif managerChoice == 4:
                empName = str(input("Please Enter The New Employee Name (Full Name): "))
                newFirst, newLast = empName.split(" ")
                newNum = str(input("Please Enter Their Phone Number: "))
                newPay = int(input("Please Enter Their Salary: "))
                newEmpString = f"{newFirst}-{newLast}-{newNum}-{newPay}"
                newName = str(input("Please Enter The Name of The New Employeee: "))
                listItems(jobTitle)
                userChoice = int(input(f"Which Role Would You Like To Give The New Employee?: 1 - {len(jobTitles)} \n Enter Here: "))
                newJobTitle = jobTitles[userChoice - 1]
                Manager.fromString(f"{newFirst}-{newLast}-{newNum}-{newPay}", newName, newJobTitle)
            elif managerChoice == 0:
                currentState = State.Login
        elif currentState == State.CEOMenu:                            # CEO Menu
            CEOChoice = int(input("Please Choose What You Would Like to Do: \n 1 - View Employees \n 2 - Add Employee \n 3 - Remove Employee \n 4 - Change Company Name \n 5 - Enter Floormart Management Mode \n 0 - Exit \n Enter Here: "))
            if CEOChoice == 1:
                print("Employees:")
                listItems(employees)
            elif CEOChoice == 2:
                print(addEmployee(employee))
            elif CEOChoice == 3:
                print(removeEmployee(employee))
            elif CEOChoice == 4:
                newCompany = input("Please Enter The New Company Name: ")
                print(changeCompany(company, newCompany))
            elif CEOChoice == 5:
                currentState = State.FloormartManagementMode
            elif CEOChoice == 0:
                currentState = State.Login
        elif currentState == State.JanitorMenu:                         # Janitor Menu
            janitorChoice = int(input("Please Choose What You Would Like to Do: \n 1 - View Cleaning List \n 2 - Add Cleaning Item \n 3 - Remove Cleaning Item \n 0 - Exit \n Enter Here: "))
            if janitorChoice == 1:
                print("Cleaning List:")
                listItems(cleans)
            elif janitorChoice == 2:
                print(addCleaning(cleans, item))
            elif janitorChoice == 3:
                print(completedCleaning(cleans))
            elif janitorChoice == 0:
                currentState = State.Login
        elif currentState == State.SecurityGuardMenu:                   # Security Guard Menu
            securityGuardChoice = int(input("Please Choose What You Would Like to Do: \n 1 - View Security Areas \n 2 - Add Security Area \n 3 - Remove Security Area \n 0 - Exit \n Enter Here: "))
            if securityGuardChoice == 1:
                print("Security Areas:")
                listItems(secures)
            elif securityGuardChoice == 2:
                print(addSecurityArea(secures, item))
            elif securityGuardChoice == 3:
                print(removeSecurityArea(secures))
            elif securityGuardChoice == 0:
                currentState = State.Login
        elif currentState == State.ITSupportMenu:                       # IT Support Menu
            pass
        elif currentState == State.FloormartManagementMode:             # Floormart Management Mode
            floormartManagementModeChoice = int(input("Please Choose What You Would Like to Do: \n 1 - View Liquid Assets \n 2 - Add Liquid Asset \n 3 - Sell Liquid Asset \n 4 - Add Expense \n 5 - Remove Expense \n 6 - Create Deal \n 0 - Exit \n Enter Here: "))
            if floormartManagementModeChoice == 1:
                print("Liquid Assets:")
                listItems(Floormart.liquidAssets)
            elif floormartManagementModeChoice == 2:
                asset = input("Please Enter The Name of The Asset: ")
                moneyWorth = int(input("Please Enter The Value of The Asset: "))
                Floormart.addLiquidAsset(asset, moneyWorth, Floormart.liquidAssets)
                print("Asset Added.")
            elif floormartManagementModeChoice == 3:
                Floormart.sellLiquidAsset(Floormart.liquidAssets, Floormart.cashOnHand)
            elif floormartManagementModeChoice == 4:
                expense = input("Please Enter The Name of The Expense: ")
                amount = int(input("Please Enter The Amount of The Expense: "))
                Floormart.addExpense(expense, amount, Floormart.expenses)
                print("Expense Added.")
            elif floormartManagementModeChoice == 5:
                Floormart.removeExpense(Floormart.expenses)
            elif floormartManagementModeChoice == 6:
                money = int(input("Please Enter The Amount of Money You Would Like to Trade: "))
                dealChoice = int(input("Would You Like to Trade an Asset? \n 1 - Yes \n 2 - No \n Enter Here: "))
                if dealChoice == 1:
                    Floormart.createDeal(Floormart.company, Floormart.rival_companies, money, True)
                elif dealChoice == 2:
                    Floormart.createDeal(Floormart.company, Floormart.rival_companies, money)
            elif floormartManagementModeChoice == 0:
                currentState = State.CEOMenu
        elif currentState == State.Exit:                                # Exit
            break

if __name__ == "__main__":
    main()