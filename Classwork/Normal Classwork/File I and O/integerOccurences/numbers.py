def evenCalculator(number: int):
    check = number % 2

    if check == 0:
        return True
    else:
        return False


evenNumbers = []

with open("Normal Classwork\File I and O\integerOccurences\integer.txt", "r") as file:
    data = file.read()

data = data.split(", ")

for num in data:
    num = int(num)
    if evenCalculator(num) is True:
        evenNumbers.append(num)
    else:
        pass

print(evenNumbers)