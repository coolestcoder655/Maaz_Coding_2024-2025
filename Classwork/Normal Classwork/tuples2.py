# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [1,2,3,2,1]
list2 = [1, "abc", "abc", 1, 5]

def palindromeChecker(listToCheck):
    rListToCheck = listToCheck.copy()
    rListToCheck.reverse()
    if rListToCheck == listToCheck:
        print(listToCheck, "is indeed a palindrome.")
    else:
        print(listToCheck, "is not a palindrome")

# Check Both Lists

palindromeChecker(list1)
palindromeChecker(list2)