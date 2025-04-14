from os import system as terminal

def turnIntoInt(num: float):
    if int(num) == num:
        return int(num)
    else:
        return float(num)

def clearScreen():
    terminal("cls")