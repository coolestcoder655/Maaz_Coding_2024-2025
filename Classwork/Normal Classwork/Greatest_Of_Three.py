# WAP to find the greatest of 3 numbers entered by the user.

num = int(input("Please enter the first number to be checked!:"))
num1 = int(input("Please enter the second number to be checked!:"))
num2 = int(input("Please enter the third number to be checked!:"))

if (num >= num1 and num >= num2):
    print("The first number is the greatest.")
elif (num1 >= num and num1 >= num2):
    print("The second number is the greatest.")
else:
    print("The third number is the greatest.")