# Question: Write a Python program that asks the user for their full name and then:
# Prints the number of characters in their name.
# Capitalizes the first letter of each word in their name.
# Replaces any spaces in their name with underscores.

fullName = input("Please enter your full name:")


print(f"Length: {len(fullName)}")
fullName = fullName.title()
fullName = fullName.replace(" ", "_")
print(f"Name: {fullName}")