# WAP to ask the user for a number and check if it's a palindrome using a while loop

def palindromeChecker(toCheck):
    rToCheck = ""
    for x in toCheck:               # Unneccesary
        rToCheck = x + rToCheck

    if toCheck == rToCheck:       # Effecient Way To Check "toCheck == toCheck[: : -1]"
        return("Is a Palindrome")
    else:
        return("Not A Palindrome")


num = input("Enter a Number to Be Checked: ")

print(palindromeChecker(num))

