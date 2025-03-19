# WAP to ask a user for a string and reverse.

string = input("String?: ")
reversedString = ""

for x in string:
    reversedString = x + reversedString

print(reversedString)