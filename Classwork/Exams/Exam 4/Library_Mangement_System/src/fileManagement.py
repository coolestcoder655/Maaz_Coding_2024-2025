from json import load, dump

def truncateFile():
    with open("books.json", "w") as file:
        file.write("")

def loadBooks():
    with open("books.json", "r") as file:
        data = load(file)
        data = data["books"]

    return data

def writeBooks(books):
    truncateFile()

    data = {}

    for book in books:
        data[book.ISBN] = {
            "title": book.title,
            "author": book.author,
            "bookStatus": book.bookStatus,
            "borrower": book.borrower
        }

    with open("books.json", "r") as file:
        dump({"books": data}, file)