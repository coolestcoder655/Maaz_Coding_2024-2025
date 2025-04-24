from os import system, name

def clearOutput():
    system("cls" if name == "nt" else "clear")  # Clears The Output Of The Terminal
    return