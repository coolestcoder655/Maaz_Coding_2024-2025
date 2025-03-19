from typing import Optional
from time import sleep
from random import randint
from enum import Enum

class Floormart():

    def __init__(self, liquidAssets: list, revenue): # Net Worth: List With Tuple For Each Asset, Name and Value
        self.company = Floormart
        self.liquidAssets = liquidAssets
        self.cashOnHand = 1000000000
        self.expenses = [] # Add Tuples For Name and Amount Of Expense
        self.employees = []
        self.rival_companies = [
            "Ceilingmart",
            "Wallmart",
            "Cornermart",
            "Stairmaster Pro",
            "VacuumMart",
            "The Rugrats",
            "\"No Floor Necessary\" Inc."
            ]

    # Money Functions
    @property
    def revenue(self):
        return f"${revenue}"
    
    @property
    def totalProfit(self):
        totalExpenses = 0
        for x in expenses:
            totalExpenses += x[1]
        return f"${revenue - totalExpenses}"

    @property
    def netWorth(self):
        total = 0
        for x in liquidAssets:
            total += x[1]
        return f"${total}"

    # ----------------

    # Employee Functions    

    @property
    def totalEmployees(self):
        return len(employees)
    
    def addEmployee(self, employee: str):
        print("Adding...")
        self.employees.append(employee)
        return "Completed."

    # Property Functions

    def addLiquidAsset(self, asset, moneyWorth, liquidAssets):
        def rollExpenses():
            return randint(1, 100000)
        
        liquidAssets.append((asset, rollExpenses()))
        return "Completed."

    def sellLiquidAsset(self, liquidAssets, cashOnHand):
        listItems(liquidAssets)
        userChoice = int(input(f"Which Item Would You Like to Sell?: 1 - {len(liquidAssets)} \n Enter Here: "))
        moneyWorth = liquidAssets[userChoice - 1][1]
        self.cashOnHand += moneyWorth
        liquidAssets.pop(userChoice - 1)
        return "Completed."

    # Expense Functions

    def addExpense(self, expense, amount, expenses):
        expenses.append((expense, amount))
        return "Completed."
    
    def removeExpense(self, expenses):
        listItems(expenses)
        userChoice = int(input(f"Which Item Would You Like to Remove?: 1 - {len(expenses)} \n Enter Here: "))
        expenses.pop(userChoice - 1)
        return "Completed."

    # List Functions

    def listEmployees(self):
        listItems(employees)

    def listAssets(self):
        listItems(liquidAssets)
    
    def listExpenses(self):
        listItems(expenses)
    
    # Deal Function

    def createDeal(self, company, rival_companies, money, assets: bool = False):
        rivalCompany = rival_companies[randint(0, len(rival_companies) - 1)]
        totalMoneyToTrade = 0
        if assets:
            listItems(assets, 1)
            userChoice = int(input(f"Which Asset Would You Like to Trade?: 1 - {len(assets)} \n Enter Here: "))
            asset = assets[userChoice - 1]
            totalMoneyToTrade += asset[1]
            assets.pop(userChoice - 1)
        totalMoneyToTrade += money
        self.cashOnHand -= totalMoneyToTrade
        print(f"Trade Completed. {company} has traded with {rivalCompany}. Economical Values: \n {company}: \n Cash: -${totalMoneyToTrade}; Asset Bartered: {asset[0]} \n {rivalCompany}: \n Cash: +${totalMoneyToTrade}; Asset Gained: {asset[0]}")
        return "Completed."