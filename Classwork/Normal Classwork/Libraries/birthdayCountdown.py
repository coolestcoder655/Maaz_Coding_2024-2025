# Libraries: datetime
# Scenario:
# Write a script that asks the user for their birthday in the format YYYY-MM-DD.
# Your program should then:
# Calculate how many days are left until their next birthday ✅
# Display their current age in years ✅
# If their birthday is today, print a special message ✅
# Requirements:
# Use datetime.date.today() ✅
# Use datetime.timedelta to calculate the difference ✅
# Handle date parsing using datetime.strptime() ✅
# Bonus: Ask if the user wants to see how many weeks, months, or seconds are left until their birthday. ✅

from datetime import date, timedelta
from os import system, name

daysToWeek = lambda x: x / 7
daysToMonths = lambda x: x / 30.5


def clearOutput():
    system("cls" if name == "nt" else "clear")


def birthdayCountdown(days: int, year: int, months: int):
    if year > date.today().year:
        print(f"The year \"{year}\" is greater that the current year, \"{date.today().year}\".")
    else:
        if months == 2 and days == 29:
            days = 28


        birthdayThisYearDate = date(year=date.today().year, month=months, day=days)
        birthdayThisYear = date.strftime(birthdayThisYearDate, "%m/%d/%Y") # 01242025
        todayDate = date.today()
        today = date.strftime(date.today(), "%m/%d/%Y") # 01242025
        age = year
        age = date.today().year - year

        if birthdayThisYear == today:
            print("Happy Birthday!!!")
        else:
            if birthdayThisYear < today:
                print("Birthday Has Already Passed! Wait Till Next Year!")
            else:
                timeLeft = birthdayThisYearDate - todayDate


                print("Would you like to view the days left of your birthday in...")
                print("1. Days")
                print("2. Weeks")
                print("3. Months")

                timeLeft = timeLeft.days

                choice = input("Enter your choice: ")

                clearOutput()

                if choice == "1":
                    print(f"{timeLeft} Days Left.")
                elif choice == "2":
                    print(f"{daysToWeek(timeLeft):.2f} Weeks Left.")
                elif choice == "3":
                    print(f"{daysToMonths(timeLeft):.2f} Months Left.")

        print(f"You are currently {age} years old.")


birthdayCountdown(23, 2026, 5)