number = int(input("Please Enter The Number To Be Checked:"))

if number < 0:
    print("The number you have entered is a negative.")
elif number > 0:
    print("The number you have entered is a positive.")
elif number == 0:
    print("The number you have entered is zero.")

check = number%2

if check == 0:
    print("The number you have entered is even.")
elif check != 0:
    print("The number you have entered is odd.")