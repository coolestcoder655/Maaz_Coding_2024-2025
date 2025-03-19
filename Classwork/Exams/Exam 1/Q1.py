# WAP to 
# 1. Asks the User to input two book titles
# 2. Stores the titles in a list called "books."
# 3. Concatenates the titles and prints the results
# 4. Prints the lengh of the first book title.

books = []

bookToAdd1 = input("Welcome to the library! \n Please enter the title of the book to be added to the library:")
bookToAdd2 = input("Please enter the second book to be added")


books.append(bookToAdd1)
books.append(bookToAdd2)

print(bookToAdd1, "and", bookToAdd2)
print(len(bookToAdd1))