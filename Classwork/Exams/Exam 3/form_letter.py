# Dear Frank,
# You owe us 2,000,000.00 euros. Please pay by tomorrow!
# Sincerely, The Collection Company

firstName = input("first name? ")
lastName = input("last name? ")
amountOwed = input("amount owed? ")
print(f" {firstName} {lastName} \n \n ")


def formLetter(first, last, amount):
    return f"Dear {first} {last}, \n \n You owe us {amount}. Please pay by tomorrow! \n \n Sincerely, The Collection Company"

print(formLetter(firstName, lastName, amountOwed))
