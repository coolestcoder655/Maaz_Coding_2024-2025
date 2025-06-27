# Sum of Digits
# Given an integer input, return the sum of its digits.
# Example: 245 → 2 + 4 + 5 = 11

def sumOfDigits(i: int):
    strI: str = str(i)
    digits: list[int] = list()

    for char in strI:
        if char == '-':
            continue

        char = int(char)

        digits.append(char)

    return sum(digits)