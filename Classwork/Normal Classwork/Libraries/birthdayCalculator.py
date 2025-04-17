# Ask the user for their birthday (YYYY-MM-DD), calculate how many days are left until their next birthday.
# Concepts: Date parsing, today’s date, handling leap years.
# Library: datetime

from datetime import date

def birthDayCalculator(birthdayMonth: int, birthdayDay: int) -> int:
    format = "%d%m%Y"

    todayStriped = int(date.strftime(date.today(), format=format))
    birthday = int(date.strftime(date(year=date.today().year, month=birthdayMonth, day=birthdayDay), format=format))

    timeLeft = birthday - todayStriped

    timeLeft = str(timeLeft)

    timeLeft = date(day=int(timeLeft[:2]), month=int(timeLeft[2:4]), year=int(timeLeft[4:]))

    return timeLeft

print(birthDayCalculator(1, 24))