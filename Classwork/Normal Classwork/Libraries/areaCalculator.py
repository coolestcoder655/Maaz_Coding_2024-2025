# Libraries: math
# Scenario:
# You are building a geometry assistant that helps users calculate area and perimeter for different shapes. The user should be prompted to select a shape (Circle, Rectangle, or Triangle), and then enter appropriate dimensions. Based on the input, the program should compute and return the results.
# Requirements:
# Bonus: Let the user repeat calculations until they choose to exit.

from math import pi, sqrt
from os import system, name

# circle: pi * r^2

# triangle: √[s(s-a)(s-b)(s-c)], where s = (a+b+c)/2

# rectangle/sqaure: 2(l + w)

def isInt(num: float):
    if num == int(num):
        return int(num)
    else:
        return float(num)

def inputVal(*args):
    if any([arg < 0 for arg in args]):
        raise Exception("Not Valid Input, Has To Be Positive")
    
def clearOutput():
    system("cls" if name == "nt" else "clear")

def askForNum(prompt: str) -> float:
    while True:
        try:
            num = float(input(prompt))
        except ValueError:
            print("Has To Be An Int / Float.")
            continue
        else:
            return num


circleArea = lambda radius: pi * (radius ** 2)

def rectangleArea(length: float, width: float) -> float:
    return isInt(length * width)

def triangleArea(sideA: float, sideB: float, sideC: float) -> float:
    s = (sideA + sideB + sideC) / 2
    return isInt(sqrt(s * (s-sideA) * (s-sideB) * (s-sideC)))

# ---------------------------------------------------------------------

def rectanglePerimeter(length: float, width: float) -> float:
    return isInt(2 * (length + width))

def circlePerimeter(radius: float) -> float:
    diameter = radius * 2
    return isInt(diameter * pi)

def trianglePerimeter(sideA: float, sideB: float, sideC: float) -> float:
    return isInt(sideA + sideB + sideC)

running = True

clearOutput()

while running:
    try:
        print("Calculator: ")
        print("1. Area")
        print("2. Perimeter")
        
        calculatorChoice = (input("Enter your choice: "))

        if calculatorChoice == "1":
            clearOutput()
            while True:
                print("1. Rectangle")
                print("2. Triangle")
                print("3. Circle")
                print("Ctrl + C To Exit AT ANY TIME.")

                areaChoice = (input("Enter your choice: "))

                match areaChoice:
                    case "1":
                        length = askForNum("Please enter the length of the rectangle: ")
                        width = askForNum("Please enter the width of the rectangle: ")

                        try:
                            inputVal(length, width)
                        except Exception as e:
                            print(e)
                        else:
                            print(f"{round(rectangleArea(length=length, width=width), 2):,}")

                    case "2":
                        a = askForNum("Enter the length of side A: ")
                        b = askForNum("Enter the length of side B: ")
                        c = askForNum("Enter the length of side C: ")

                        try:
                            inputVal(a, b, c)
                        except Exception as e:
                            print(e)
                        else:
                            print(f"{round(triangleArea(sideA=a, sideB=b, sideC=c), 2):,}")

                    case "3":
                        radius = askForNum("Enter the radius of the circle: ")

                        try:
                            inputVal(radius)
                        except Exception as e:
                            print(e)
                        else:
                            print(f"{round(circleArea(radius=radius), 2):,}")

                    case _:
                        print("Please enter a correct choice (ex: 1, 2, 3)")
        elif calculatorChoice == "2":
            clearOutput()
            while True:
                print("1. Rectangle")
                print("2. Triangle")
                print("3. Circle")
                print("Ctrl + C To Exit AT ANY TIME.")

                perimeterChoice = (input("Enter your choice: "))

                match perimeterChoice:
                    case "1":
                        length = askForNum("Please enter the length of the rectangle: ")
                        width = askForNum("Please enter the width of the rectangle: ")

                        try:
                            inputVal(length, width)
                        except Exception as e:
                            print(e)
                        else:
                            print(f"{round(rectanglePerimeter(length=length, width=width), 2):,}")

                    case "2":
                        a = askForNum("Enter the length of side A: ")
                        b = askForNum("Enter the length of side B: ")
                        c = askForNum("Enter the length of side C: ")

                        try:
                            inputVal(a, b, c)
                        except Exception as e:
                            print(e)
                        else:
                            print(f"{round(trianglePerimeter(sideA=a, sideB=b, sideC=c), 2):,}")

                    case "3":
                        radius = askForNum("Enter the radius of the circle: ")

                        try:
                            inputVal(radius)
                        except Exception as e:
                            print(e)
                        else:
                            print(f"{round(circlePerimeter(radius=radius), 2):,}")

                    case _:
                        print("Please enter a correct choice (ex: 1, 2, 3)")

                input("Press enter to continue...")
                clearOutput()

    except KeyboardInterrupt:
        running = False
        print("\nExiting...")
    else:
        input("Press Enter to Continue...\n")
        clearOutput()