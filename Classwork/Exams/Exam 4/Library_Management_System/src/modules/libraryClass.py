from uuid import uuid4

def checkIfEmpty(*args):
    if any(arg.strip() == "" for arg in args):
        raise Exception(f"Arguments Cannot Be An Empty String")



class Library:
    """
    A class to represent a library system. It provides functionalities
    for managing books, such as searching, borrowing, and returning books.
    """

    def __init__(self, books) -> None:
        self.books = books  # books is a dictionary with ISBN as the key

    @property
    def availableBooks(self) -> list[str]:
        """
        Retrieves a list of titles of books that are currently available.

        Returns:
            list[str]: A list of titles of books that are not borrowed.
        """
        availableBooks = [book["title"] for book in self.books.values() if book["isAvailable"]]
        return availableBooks

    def findBook(self, ISBN):
        """
        Finds and returns the book details by its ISBN.

        Args:
            ISBN (str): The ISBN of the book to search for.

        Returns:
            dict: The dictionary containing the book details if found.

        Raises:
            Exception: If the book is not found in the library.
        """

        checkIfEmpty(ISBN)

        if ISBN in self.books:
            return self.books[ISBN]  # Return the dictionary of book details directly

        raise Exception("Book Not Located In Library.")

    def findBookByTitle(self, title: str) -> dict:
        """
        Finds and returns the book details by its title.

        Args:
            title (str): The title of the book to search for.

        Returns:
            dict: The dictionary containing book details if the book is found

        Raises:
            Exception: If the book is not found in the library.
        """

        checkIfEmpty(title)

        for book in self.books.values():
            if book["title"].lower() == title.lower():
                return book
        raise Exception("Book Not Located In Library.")

    def addBook(self, title, author) -> None:
        """
        Adds a new book to the library.

        Args:
            title (str): The title of the new book.
            author (str): The author of the new book.

        Raises:
            Exception: If a book with the same title already exists in the library.
        """

        checkIfEmpty(title, author)

        if any(book["title"] == title for book in self.books.values()):
            raise Exception(f"Book with title {title} already exists in the library.")

        self.books[str(uuid4())] = {  # Add a new dictionary entry with the given ISBN
            "title": title,
            "author": author,
            "isAvailable": True,
            "borrower": None
        }

    def borrowBook(self, ISBN, borrower: str) -> None:
        """
        Borrows a book from the library by marking it as not available.

        Args:
            ISBN (str): The ISBN of the book to borrow.
            borrower (str): The name of the person borrowing the book.

        Prints:
            Message indicating if the book is already borrowed or if
            it has been successfully borrowed.
        """

        checkIfEmpty(ISBN, borrower)

        try:
            bookToBorrow = self.findBook(ISBN)  # Get the book details dictionary
        except Exception as e:
            print(e)
            return

        if not bookToBorrow["isAvailable"]:
            print(f"The book '{bookToBorrow['title']}' is already borrowed.")
            return

        if borrower.strip() == "":
            raise Exception("Borrower Cannot Be Anonymous")

        bookToBorrow["isAvailable"] = False
        bookToBorrow["borrower"] = borrower

    def returnBook(self, ISBN) -> None:
        """
        Returns a borrowed book to the library, marking it as available.

        Args:
            ISBN (str): The ISBN of the book to return.

        Prints:
            Message indicating if the book was returned successfully or
            if the book was not found in the library.
        """

        checkIfEmpty(ISBN)

        try:
            bookToReturn = self.findBook(ISBN)  # Get the book details dictionary
        except Exception as e:
            print(e)
            return

        bookToReturn["isAvailable"] = True
        bookToReturn["borrower"] = None