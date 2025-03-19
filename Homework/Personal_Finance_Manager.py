# WAP where a user can track their income, expenses, and savings. . The system should allow users to:
# • Add income with a description (e.g., salary, gift).
# • Add expenses with categories (e.g., groceries, rent, entertainment).
# • View total income, total expenses, and remaining balance.
# • Set savings goals and track progress.
# Steps:
# 1. Create lists to store income and expenses, along with their descriptions.
# 2. Allow users to add new income and expenses through a menu-driven system.
# 3. Calculate the balance after adding or subtracting entries.
# 4. Add functionality for setting a savings goal and tracking how close the user is to reaching it.
# part = 15
# whole = 25
# percentage = (part / whole) * 100
# print("Percentage:", percentage)

userIncome = 0

userExpenses = 0

afterIncomeExpenses = 0

SavingsGoal = 0


while True:
    userChoice = int(input("Welcome to the PFM (Personal Finance Manager) \n What would you like to do? \n 1 = View Total Income \n 2 = View Total Expenses \n 3 = Add Income \n 4 = Add Expenses \n 5 = Set a New Savings Goal \n 6 = View Savings Goal Progress"))

    if userChoice == 1:
        print(userIncome)
    elif userChoice == 2:
        print(userExpenses)
    elif userChoice == 3:
        x = int(input("Please add the amount of income that you are adding:"))
        userIncome = userIncome + x
    elif userChoice == 4:
        y = int(input("Please add the expenses received here:"))
        userExpenses = userExpenses + y
    elif userChoice == 5:
        SavingsGoal = int(input("Please Enter Your Saving Goal Here:"))
    elif userChoice == 6:
        afterIncomeExpenses = userIncome - userExpenses
        percentageofSG = int((afterIncomeExpenses / SavingsGoal) * 100)
        print("You have:", afterIncomeExpenses, "of your savings goal: ", SavingsGoal, ". That is about", percentageofSG, "% of your goal.")