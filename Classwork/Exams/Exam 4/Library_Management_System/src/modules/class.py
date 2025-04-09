class Library:
    books = []

    def __init__(self, books: dict[str, str, bool]):
        self.books = books # ISBN[title: "py", author: "me", isAvailable: True]


    def findBook(self, ISBN) -> dict[str, str, bool]:
        for book in self.books:
            if book == ISBN:
                return book

        raise Exception("Book Not Located In Library.")

    def addBook(self, ISBN, title, author, isAvailable):
        if ISBN in self.books:
            raise ValueError(f"Book with ISBN {ISBN} already exists in the library.")

        self.books[ISBN] = {
            "title": title,
            "author": author,
            "isAvailable": isAvailable
        }
