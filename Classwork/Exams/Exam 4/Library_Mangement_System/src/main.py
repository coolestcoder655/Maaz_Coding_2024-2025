from classes import Library, Book
from fileManagement import loadBooks
from colorama import Style, Fore, Back, init
from os import system as sys

init(autoreset=True)

library = Library(loadBooks())





def main():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.BLACK, Fore.RESET]
    styles = [Style.BRIGHT, Style.NORMAL, Style.DIM]
    backs = [Back.RED, Back.YELLOW, Back.GREEN, Back.CYAN, Back.BLUE, Back.MAGENTA, Back.BLACK, Back.RESET]

    def clearOutput():
        sys("cls")

    
    print(colors[0] + styles[0] + "Welcome To The Library Management System!!!")
    print(colors[0] + styles[0] + "-------------------------------------------")


if __name__ == "__main__":
    main()