class Library:
    def __init__(self, books) -> None:
        self.books = books  # books is a dictionary with ISBN as the key

    @property
    def availableBooks(self) -> list[str]:
        # Loop through the values of the books dictionary (each value is a book details dictionary)
        availableBooks = [book["title"] for book in self.books.values() if book["isAvailable"]]
        return availableBooks


    def findBook(self, ISBN):
        if ISBN in self.books:
            return self.books[ISBN]  # Return the dictionary of book details directly

        raise Exception("Book Not Located In Library.")

    def addBook(self, ISBN, title, author, isAvailable) -> None:
        if ISBN in self.books:
            raise ValueError(f"Book with ISBN {ISBN} already exists in the library.")

        self.books[ISBN] = {  # Add a new dictionary entry with the given ISBN
            "title": title,
            "author": author,
            "isAvailable": isAvailable,
            "borrower": None
        }

    def borrowBook(self, ISBN, borrower) -> None:
        try:
            bookToBorrow = self.findBook(ISBN)  # Get the book details dictionary
        except Exception as e:
            print(e)
            return

        if not bookToBorrow["isAvailable"]:
            print(f"The book '{bookToBorrow['title']}' is already borrowed.")
            return

        bookToBorrow["isAvailable"] = False
        bookToBorrow["borrower"] = borrower

    def returnBook(self, ISBN) -> None:
        try:
            bookToReturn = self.findBook(ISBN)  # Get the book details dictionary
        except Exception as e:
            print(e)
            return

        bookToReturn["isAvailable"] = True
        bookToReturn["borrower"] = None


# Sample book data
meBooks = {
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
obj = Library(books=meBooks)

# Add a new book and borrow it
obj.addBook(1293712, "Python", "Me", True)
obj.borrowBook(1293712, "Me")

obj.returnBook(1293712)

# Display the current state of the library
print(obj.availableBooks)