# WAP to find all the values in a list that are greater than a specified number.

specialNumber = int(input())
numsToCheck = [10, 1, -55, 100, 46]
stringLocation = 0
check = numsToCheck[stringLocation]
results = []

for x in numsToCheck:
    check = numsToCheck[stringLocation]

    if specialNumber < check:
        results.append(check)
    stringLocation = stringLocation + 1
print(results)