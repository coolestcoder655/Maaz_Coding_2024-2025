# Check Palindrome
# Write a program to check if a given string is a palindrome (same forward and backward).

def palindromeChecker(s: str):
    r: str = f'{s}'[::-1]

    return s == r