# Write a  Python program to create a  calculator class. Include methods for basic arithmetic operations.

# Square, Sqaure Root, Cube

from math import sqrt

class Calculator():
    def __init__(self):
        pass

    def askForNum(self) -> int:
        num1 = int(input("Enter A Number: "))
        num2 = int(input("Enter A Number: "))

        return num1, num2

    def askforOne(self) -> int:
        num1 = int(input("Enter A Number: "))

        return num1

    def add(self):
        num1, num2 = self.askForNum()

        return (num1 + num2)

    def subtract(self):
        num1, num2 = self.askForNum()

        return (num1 - num2)

    def multiply(self):
        num1, num2 = self.askForNum()

        return (num1 * num2)
    
    def divide(self):
        num1, num2 = self.askForNum()

        return (num1 / num2)

    def square(self):
        num1 = self.askforOne()

        return (num1 ** 2)
    
    def cube(self):
        num1 = self.askforOne()

        return (num1 ** 3)
    
    def root(self, isRound: bool):
        num1 = self.askforOne()

        if isRound:
            return (round(sqrt(num1), 2))
        else:
            return (sqrt(num1))
        
    
newCalculator = Calculator()

print(newCalculator.add())

print(newCalculator.subtract())

print(newCalculator.multiply())

print(newCalculator.divide())

print(newCalculator.square())

print(newCalculator.cube())

print(newCalculator.root(False))

print(newCalculator.root(True))