from colorama import Style, Fore, init, Back
from modules.libraryClass import Library
from os import system, name

init(autoreset=True)

Fores = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
Styles = [Style.BRIGHT, Style.DIM, Style.NORMAL]

def main() -> None:
    booksInLibrary = {
        "987654321": {
            "title": "JavaScript",
            "author": "You",
            "isAvailable": True,
            "borrower": None
        },
        "111213141": {
            "title": "Java",
            "author": "They",
            "isAvailable": True,
            "borrower": None
        },
        "314151617": {
            "title": "C++",
            "author": "Us",
            "isAvailable": True,
            "borrower": None
        }
    }

    # Create a Library object
    obj = Library(books=booksInLibrary)

    try:
       while True:
            system('cls')
            print(Fores[2] + Styles[0] + "Welcome To The Public Library Kiosk.")
            print(Fores[2] + Styles[0] + "------------------------------------")

            print("\nChoose What You Would Like To Do:")

            indent = "  "

            print(Fores[1] + indent + "1. View Available Books")
            print(Fores[3] + indent + "2. Add New Book")
            print(Fores[2] + indent + "3. Borrow Book")
            print(Fores[4] + indent + "4. Return Book")
            print(Fores[0] + Styles[1] + indent + "⚠️ Ctrl + C to Exit At Any Time ⚠️")

            choice = input("\nEnter Your Choice: ")

            if choice == "1":
                print(obj.availableBooks)

            elif choice == "2":
                try:
                    newBookTitle = str(input("Enter Title Of New Book: "))
                    newBookAuthor = str(input("Enter Author Of New Book: "))

                    obj.addBook(newBookTitle, newBookAuthor)
                except Exception as e:
                    print(e)

            elif choice == "3":
                try:
                    bookToBorrow = str(input("Enter the title of the book you want to borrow: "))
                    borrower = str(input("Enter your name: "))

                    bookToBorrow = obj.findBookByTitle(bookToBorrow)
                    for x in obj.books:
                        if obj.books[x] == bookToBorrow:
                            bookToBorrow = x
                            break

                    obj.borrowBook(bookToBorrow, borrower)
                except Exception as e:
                    print(e)

            elif choice == "4":
                try:
                    bookToReturn = str(input("Enter the title of the book you want to return: "))
                    bookToReturn = obj.findBookByTitle(bookToReturn)
                    for x in obj.books:
                        if obj.books[x] == bookToReturn:
                            bookToReturn = x

                    obj.returnBook(bookToReturn)
                except Exception as e:
                    print(e)

            else:
                print("Invalid Choice. Please Try Again.")

            input("\nPress Enter To Continue...")

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == '__main__':
    main()