class Solution:
    def calculate(num1: str, op: str, num2: int) -> int:
        try:
            match op:
                case "+":
                    return num1 + num2
                case "-":
                    return num1 - num2
                case "*":
                    return num1 * num2
                case "x":
                    return num1 * num2
                case "/":
                    return num1 / num2
                case "//":
                    return num1 // num2
                case _:
                    print("Operation Not Supported Or Operation Invalid.")
                    raise NotImplementedError
        except NotImplementedError as n:
            print(n)

print(Solution.calculate(100, "//", 10))