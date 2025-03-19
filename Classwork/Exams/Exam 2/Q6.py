# • Question: Write a program that:
# 1. Asks the user for their age and the year they were born. 
# 2. Calculates their current age based on the current year 
# (assumed to be 2024). 
# 3. Formats and prints a message like: "You are 25 years old, 
# born in 1999


age = int(input("What's Your Age? \n "))

age2Check = 0

bornIn = int(input("What Was The Year You Were Born? \n "))

while bornIn != 2024:
    bornIn += 1
    age2Check += 1

if age2Check != age:
    print("IM ANGWY!!!!! YOU ARE ", age2Check, "YEARS OLD!!!")
else:
    print("YAY! YOU WEREN'T LYING!!!!!")