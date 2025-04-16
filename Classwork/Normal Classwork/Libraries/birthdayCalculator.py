# Ask the user for their birthday (YYYY-MM-DD), calculate how many days are left until their next birthday.
# Concepts: Date parsing, today’s date, handling leap years.
# Library: datetime

from datetime import date

def birthdayCalculator(inputMonth: int, inputDay: int):
    today = date.today()
    birthday = date.today()
    birthday = birthday.replace(year=)

    print(today - birthday)


birthdayCalculator()