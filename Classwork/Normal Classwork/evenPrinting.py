# WAP to print all even numbers between 1 and a user inputted number and the sum of them all together.

numbers = []
evenNumbers = []
numSum = 0

numRange = int(input("Range?: 1 - ")) + 2

for x in range(numRange):
    numbers.append(x)

for x in numbers:
    if x %2 == 0:
        evenNumbers.append(x)

print(evenNumbers)

for x in evenNumbers:
    numSum = numSum + x
print(f"Sum: {numSum}")