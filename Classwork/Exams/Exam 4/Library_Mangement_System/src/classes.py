from fileManagement import writeBooks

class Library():
    books = []
    def __init__(self, books: dict = {}): # {ISBN: {title, author, bookStatus}}
        self.books = books
        self.initalizeBooks()

    def initalizeBooks(self) -> None:
        for book in self.books:
            newBook = Book(ISBN=book, title=self.books[book].get("title", "Untitled"), author=self.books[book].get("author", "Jane Doe"), bookStatus=self.books[book].get("bookStatus", True), borrower=self.books[book].get("borrower", "John Doe"))
            self.books.pop(self.books.index(book))

    def addNewBook(self) -> None:
        newISBN = input("Please enter the ISBN for the new book: ")
        newTitle = input("Please enter the title of the new book: ")
        newAuthor = input("Please enter the author of the new book: ")
        newBookStatus = True

        newBook = Book(ISBN=newISBN, title=newTitle, author=newAuthor, bookStatus=newBookStatus)

    def __str__(self):
        indent = "    "
        for book in self.books:
            print(book.ISBN)
            print(indent + f"Title: {book.title}")
            print(indent + f"Created By: {book.author}")
            print(indent + f"Book Status: {book.bookStatus}")
            print(indent + f"Borrower: {book.borrower}" if not book.bookStatus else print("", end=""))


    def __del__(self):
        writeBooks(self.books)

class Book():
    def __init__(self, ISBN: str, title: str = "Untitled", author: str = "Jane Doe", bookStatus: bool = True, borrower: str = "John Doe"):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.bookStatus = bookStatus
        self.borrower = borrower
        Library.books.append(self)

    
    def borrowBook(self):
        if self.bookStatus:
            name = input("Please enter your name for the record: ")
            self.bookStatus = False
            self.borrower = name
        else:
            print("Book Already Checked Out.")

    def returnBook(self):
        if not self.bookStatus():
            self.bookStatus = True
            self.borrower = None
        else:
            print("Book Has Already Been Returned.")