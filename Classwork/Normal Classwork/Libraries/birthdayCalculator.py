# Ask the user for their birthday (YYYY-MM-DD), calculate how many days are left until their next birthday.
# Concepts: Date parsing, today’s date, handling leap years.
# Library: datetime

from datetime import date

def birthDayCalculator(birthdayYear: int, birthdayMonth: int, birthdayDay: int) -> int:
    format = "%d%m%Y"

    today = int(date.strftime(date.today(), format=format))
    birthday = int(date.strftime(date(year=birthdayYear, month=birthdayMonth, day=birthdayDay), format=format))

    return birthday - today

print(birthDayCalculator(2012, 1, 24))