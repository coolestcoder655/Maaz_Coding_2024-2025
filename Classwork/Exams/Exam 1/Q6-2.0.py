uniqueNumbers = []
numbers = [1,2,3,2,4,7,9,4,1]
for x in numbers:
    if x not in uniqueNumbers:
        uniqueNumbers.append(x)
print(uniqueNumbers)