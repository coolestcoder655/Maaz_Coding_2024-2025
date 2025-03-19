# Write a Python program that asks the user for their favorite number and checks if it is divisible by both 2 and 3.

# - If it is divisible by both, print `"Your number is divisible by both 2 and 3"`.

# - If it is divisible by only one of them, print `"Your number is divisible by 2"`, or `"Your number is divisible by 3"`, depending on the case.

# - If it is divisible by neither, print `"Your number is not divisible by 2 or 3"`.

favNum = int(input("Enter our favorite number!!!"))

if favNum%2 == 0 and favNum%3 == 0:
    print("Your number is divisible by both 2 and 3!!!")
elif favNum %2 == 0:
    print("Your number is divisible by 2!!!")
elif favNum %3 == 0:
    print("Your number is divisible by 3!!!")
else:
    print("Your number is not divisible by 2 or 3.")