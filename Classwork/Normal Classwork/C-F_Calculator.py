#  Write a program that takes a temperature input from the user and converts it from Celsius to Fahrenheit or Fahrenheit to Celsius based on user choice.

# F = (C x 9/5) + 32
# C = (F - 32) x 5/9

answer = input("Are you using converting to C or F?")

if answer == "C" or "c":
    celsius = int(input("Please write the tempature(C) to be changed."))

    F = (celsius * 9/5) + 32

    print(int(F))
elif answer == "F" or "f":
    F = int(input("Please write the temp(F) to be changed."))

    C = (F - 32) * 5/9

    print(int(C))
else:
    print("Please use the letters 'C' for Celsius or 'F' for Fahrenheit.!!!")