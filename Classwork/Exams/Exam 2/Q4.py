# Question: Create a Python program that:
# 1. Asks the user for three favorite fruits and stores them in a list 
# called fruits.
# 2. Prints the second fruit in the list. 
# 3. Checks if “banana” is in the list and prints a message 
# accordingly.

favFruits = []

for x in range(3):
    favFruits.append(input("Please Enter Your Favorite Fruits:"))

print(favFruits[1])

if "banana" in favFruits:
    print("There is a 'banana' in the list.")
else:
    print("There is no 'banana' in the list.")